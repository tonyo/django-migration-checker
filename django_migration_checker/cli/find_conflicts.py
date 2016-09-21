#!/usr/bin/env python
import argparse

from django_migration_checker import get_conflicts


def create_parser():
    parser = argparse.ArgumentParser(
        description='Find migration conflicts in Django projects.'
    )
    parser.add_argument('apps_dir', metavar='APPS_DIR',
                        help='directory with Django applications')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    conflicts = get_conflicts(args.apps_dir)
    if conflicts:
        print(conflicts)
    else:
        print('No conflicts detected.')
