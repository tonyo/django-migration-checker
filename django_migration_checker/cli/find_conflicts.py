#!/usr/bin/env python
import sys
import argparse

from django_migration_checker import get_conflicts


def create_parser():
    parser = argparse.ArgumentParser(description="Find migration conflicts in Django projects.")
    parser.add_argument(
        "apps_dirs",
        metavar="APPS_DIRS",
        nargs="+",
        help="one or more directory with Django applications",
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    exit_1 = False
    for dir in args.apps_dirs:
        if len(args.apps_dirs) > 1:
            print(dir + ":")

        conflicts = get_conflicts(dir)
        if conflicts:
            print(conflicts)
            exit_1 = True
        else:
            print("No conflicts detected.")
    if exit_1:
        sys.exit(1)
