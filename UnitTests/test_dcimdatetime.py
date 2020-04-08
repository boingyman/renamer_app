from unittest import TestCase
import dcimdatetime
from renaming_exceptions import *


class TestRename(TestCase):
    def test_rename1_essential(self):  # Test expected input.
        testString = "20000101_120123"
        expectedString = "2000 01 01 - 12_01_23"

        result = dcimdatetime.rename(testString)

        self.assertEqual(result, expectedString)

    def test_rename2_essential(self): # Test expected input.
        testString = "20000101_120123-just the best ok"
        expectedString = "2000 01 01 - 12_01_23-just the best ok"

        result = dcimdatetime.rename(testString)

        self.assertEqual(result, expectedString)

    def test_rename3(self):  # Test unexpected, but similar input.
        testString = "2010042_12403"

        self.assertRaises(InvalidFileNameError, dcimdatetime.rename, testString)

    def test_rename4(self):  # Test unexpected input.
        testString = "something really wrong"

        self.assertRaises(InvalidFileNameError, dcimdatetime.rename, testString)

    def test_rename5(self):  # Test wrong type.
        testInput = 23

        self.assertRaises(Exception, dcimdatetime.rename, testInput)
