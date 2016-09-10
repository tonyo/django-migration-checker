#!/usr/bin/env python
import os
import re


def extract_dependencies(file_path):
    """
    Parse the file contents and return the list of dependencies.
    """
    file_contents = open(file_path).read()
    match = re.search(r"""^\s+dependencies [^\[]+
                          \[
                          ([^\]]*)
                          \]""",
                      file_contents,
                      flags=re.VERBOSE | re.MULTILINE)
    if not match:
        return []

    deps = match.group(1).strip()
    if not deps:
        return []

    match_iter = re.finditer(r"""\(
                                 '([^']+)'
                                 ,\s*
                                 '([^_][^']+)'
                                 \)""",
                             deps,
                             flags=re.VERBOSE)
    return [(match.group(1), match.group(2)) for match in match_iter]


def find_apps_with_migrations(app_dir):
    """
    Return a list of tuples, where each tuple has three elements:
    - app
    - migration file (no path)
    - full path to migration file
    """
    res = []
    for entry in os.listdir(app_dir):
        entry_path = os.path.join(app_dir, entry)
        # Skip if not a directory or there's no 'migration' dir
        if (not os.path.isdir(entry_path) or
                'migrations' not in os.listdir(entry_path)):
            continue

        migrations_dir = os.path.join(entry_path, 'migrations')
        for migration_file in os.listdir(migrations_dir):
            # Skip __init__.py and non-Python files
            if (migration_file.startswith('__') or
                    not migration_file.endswith('.py')):
                continue
            full_path = os.path.join(migrations_dir, migration_file)
            res.append(((entry, migration_file[:-3]), full_path))
    return res


def get_conflicts(app_dir):
    # Check that for every app there's at most one leaf node
    migrations_list = find_apps_with_migrations(app_dir)
    leaves = {x[0] for x in migrations_list}

    # Detect leaves
    for _, migration_file in migrations_list:
        dep_list = extract_dependencies(migration_file)
        for dep in dep_list:
            if dep in leaves:
                leaves.remove(dep)

    # Check conflicts
    app_to_leaves = {}
    for app, migration in leaves:
        app_to_leaves.setdefault(app, []).append(migration)

    conflicts = list(filter(lambda t: len(t[1]) > 1, app_to_leaves.items()))

    # Sort output
    sorted_conflicts = map(
        lambda app_conflicts: (app_conflicts[0], sorted(app_conflicts[1])),
        conflicts
    )
    return list(sorted_conflicts)
