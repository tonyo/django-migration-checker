#!/usr/bin/env python
import sys
import unittest

from django_migration_checker.base import extract_list


class TestExtractList(unittest.TestCase):
    def test_basic_single_quote(self):
        content = """
            dependencies = [
                ('llamas', '0001_one'),
            ]
        """
        assert [("llamas", "0001_one")] == extract_list("dependencies", content)

    def test_basic_double_quote(self):
        content = """
            dependencies = [
                ("llamas", "0001_one"),
            ]
        """
        assert [("llamas", "0001_one")] == extract_list("dependencies", content)

    def test_basic_compact_style(self):
        content = """
            dependencies=[('llamas','0001_one')]
        """
        assert [("llamas", "0001_one")] == extract_list("dependencies", content)

    def test_multi_dependencies_single_quote(self):
        content = """
            dependencies = [
                ('llamas', '0001_one'),
                ('llamas', '0002_two'),
                ('llamas', '0003_three'),
            ]
        """
        assert [
            ("llamas", "0001_one"),
            ("llamas", "0002_two"),
            ("llamas", "0003_three"),
        ] == extract_list("dependencies", content)

    def test_multi_dependencies_double_quote(self):
        content = """
            dependencies = [
                ("llamas", "0001_one"),
                ("llamas", "0002_two"),
                ("llamas", "0003_three"),
            ]
        """
        assert [
            ("llamas", "0001_one"),
            ("llamas", "0002_two"),
            ("llamas", "0003_three"),
        ] == extract_list("dependencies", content)


if __name__ == "__main__":
    sys.exit(unittest.main())
