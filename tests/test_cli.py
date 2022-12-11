#!/usr/bin/env python
import sys
import unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import django_migration_checker.cli.find_conflicts as find_conflicts
from django_migration_checker.cli.find_conflicts import create_parser


class TestFindMigrationsCliChecker(unittest.TestCase):
    def setUp(self):
        self.parser = create_parser()
        self.apps_dir_input = "example_app_dir"
        self.valid_parsed_args = self.parser.parse_args([self.apps_dir_input])

    def test_with_empty_args(self):
        """
        User passes no args, should fail with SystemExit
        """
        self.assertRaises(SystemExit, self.parser.parse_args, [])

    def test_app_dir_argument(self):
        """
        User passes one argument => APPS_DIR
        """
        args = self.valid_parsed_args

        assert args.apps_dirs == [self.apps_dir_input]

    @patch("django_migration_checker.cli.find_conflicts.get_conflicts")
    @patch("argparse.ArgumentParser.parse_args")
    def test_cli_passes_args(self, m_parse_args, m_get_conflicts):
        m_parse_args.return_value = self.valid_parsed_args

        self.assertRaises(SystemExit, find_conflicts.main)

        m_get_conflicts.assert_called_with(self.apps_dir_input)


if __name__ == "__main__":
    sys.exit(unittest.main())
