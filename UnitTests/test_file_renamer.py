from unittest import TestCase
import file_renamer
import io
import sys
import os


class TestFileRenamer(TestCase):
    def test_run1_essential(self):  # Test expected input and print output.
        output = io.StringIO()
        temp = sys.stdout  # In unit tests, stdout is an object that does not have the method 'getvalue()'.
        sys.stdout = output

        file_renamer.run('./testing_script.py', ["Correct Test Name.txt"], isPrinting=True)

        sys.stdout = temp  # Reassign the old stdout object instead of 'sys.__stdout__'.

        self.assertEqual("Resulting Name.txt\n", output.getvalue())

    def test_run2_essential(self):
        filePath = os.path.abspath('./Correct Test Name.txt')

        os.fdopen(os.open(filePath, os.O_CREAT)).close()

        file_renamer.run('./testing_script.py', [filePath])

        self.assertTrue(os.path.isfile(os.path.join(os.path.dirname(filePath), "Resulting Name.txt")))

        os.remove(os.path.join(os.path.dirname(filePath), "Resulting Name.txt"))

    def test_run3(self):
        self.assertRaises(FileNotFoundError, file_renamer.run, './non-existent file name.py', [], False, True)

    #def test_run4_essential(self): # Multiple files
    #    filePaths = [os.path.abspath('./Correct Test Name.txt'), os.path.abspath('./Another/Correct Test Name.txt')]
    #
    #    os.fdopen(os.open(filePaths[0], os.O_CREAT)).close()
    #    os.fdopen(os.open(filePaths[1], os.O_CREAT)).close()
    #
    #    file_renamer.run('./testing_script.py', filePaths)
    #
    #    # TODO: Using `self.assertTrue` would result in the enclosed expression to evaluate false for some reason...
    #    # Unsure if this is a problem with the script or `self.assertTrue`.
    #    self.assertEqual(os.path.isfile(os.path.join(os.path.dirname(filePaths[0]), "Resulting Name.txt")), True)
    #    self.assertEqual(os.path.isfile(os.path.join(os.path.dirname(filePaths[1]), "Resulting Name.txt")), True)
    #
    #    os.remove(os.path.join(os.path.dirname(filePaths[0]), "Resulting Name.txt"))
    #    os.remove(os.path.join(os.path.dirname(filePaths[1]), "Resulting Name.txt"))
