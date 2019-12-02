from unittest import TestCase
import file_renamer
import io
import sys
import os


class TestFileRenamer(TestCase):
    def test_run1(self):  # Test expected input and print output.
        output = io.StringIO()
        temp = sys.stdout  # In unit tests, stdout is an object that does not have the method 'getvalue()'.
        sys.stdout = output

        file_renamer.run('./testing_script.py', ["Correct Test Name.txt"], True)

        sys.stdout = temp  # Reassign the old stdout object instead of 'sys.__stdout__'.

        self.assertEqual("Resulting Name.txt\n", output.getvalue())

    def test_run2(self):
        filePath = os.path.abspath('./Correct Test Name.txt')

        os.fdopen(os.open(filePath, os.O_CREAT)).close()

        file_renamer.run('./testing_script.py', [filePath])

        self.assertTrue(os.path.isfile(os.path.join(os.path.dirname(filePath), "Resulting Name.txt")))

        os.remove(os.path.join(os.path.dirname(filePath), "Resulting Name.txt"))

    def test_run3(self):
        self.assertRaises(FileNotFoundError, file_renamer.run, './non-existent file name.py', [], True)