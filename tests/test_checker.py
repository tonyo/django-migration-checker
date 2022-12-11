#!/usr/bin/env python
import os
import sys
import unittest

from django_migration_checker import get_conflicts

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_DATA_PATH = os.path.join(SCRIPT_PATH, "test_data")


class TestDjangoMigrationChecker(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_apps(self):
        assert [] == get_conflicts(TEST_DATA_PATH)

    def test_no_conflicts(self):
        test_dir = os.path.join(TEST_DATA_PATH, "01_no_conflicts")
        assert [] == get_conflicts(test_dir)

    def test_basic_conflict(self):
        test_dir = os.path.join(TEST_DATA_PATH, "02_basic_conflicts")
        assert [("alpacas", ["0001_initial", "0002_new"])] == get_conflicts(test_dir)

    def test_inter_app_conflict(self):
        test_dir = os.path.join(TEST_DATA_PATH, "03_inter_app_conflict")
        assert [("llamas", ["0001_initial", "0002_new_one"])] == get_conflicts(test_dir)

    def test_no_app_dir(self):
        test_dir = os.path.join(TEST_DATA_PATH, "02_basic_conflicts")
        os.chdir(test_dir)
        assert [("alpacas", ["0001_initial", "0002_new"])] == get_conflicts()

    def test_squashed_no_conflict(self):
        test_dir = os.path.join(TEST_DATA_PATH, "04_squashed_no_conflict")
        assert [] == get_conflicts(test_dir)

    def test_squashed_basic_conflict(self):
        test_dir = os.path.join(TEST_DATA_PATH, "05_squashed_basic_conflict")
        result = [("llamas", ["0001_squashed_0002_auto_20190509_1610", "0002_new_one"])]
        assert result == get_conflicts(test_dir)

    def test_no_conflicts_double_quotes(self):
        test_dir = os.path.join(TEST_DATA_PATH, "06_no_conflicts_double_quotes")
        assert [] == get_conflicts(test_dir)


if __name__ == "__main__":
    sys.exit(unittest.main())
