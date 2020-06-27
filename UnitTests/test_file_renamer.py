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

        file_renamer.run('./testing_script.py', ["Correct Test Name1.txt"], isPrinting=True)

        sys.stdout = temp  # Reassign the old stdout object instead of 'sys.__stdout__'.

        self.assertEqual("Resulting Name1.txt", output.getvalue())

    def test_run2_essential(self):
        filePath = os.path.abspath('./Correct Test Name.txt')

        os.fdopen(os.open(filePath, os.O_CREAT)).close()

        file_renamer.run('./testing_script.py', [filePath])

        self.assertTrue(os.path.isfile(os.path.join(os.path.dirname(filePath), "Resulting Name.txt")))

        os.remove(os.path.join(os.path.dirname(filePath), "Resulting Name.txt"))

    def test_run3_essential(self):  # Multiple files
        filePaths = [os.path.abspath('./Correct Test Name.txt'), os.path.abspath('./Another/Correct Test Name.txt')]

        os.fdopen(os.open(filePaths[0], os.O_CREAT)).close()
        os.makedirs(os.path.abspath('./Another'))
        os.fdopen(os.open(filePaths[1], os.O_CREAT)).close()

        file_renamer.run('./testing_script.py', filePaths)

        # TODO: Using `self.assertTrue` would result in the enclosed expression to evaluate false for some reason...
        # Unsure if this is a problem with the script or `self.assertTrue`.
        self.assertEqual(os.path.isfile(os.path.join(os.path.dirname(filePaths[0]), "Resulting Name.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(os.path.dirname(filePaths[1]), "Resulting Name.txt")), True)

        os.remove(os.path.join(os.path.dirname(filePaths[0]), "Resulting Name.txt"))
        os.remove(os.path.join(os.path.dirname(filePaths[1]), "Resulting Name.txt"))
        os.removedirs(os.path.abspath('./Another'))

    def test_run4_essential(self):  # Single directory, multiple files
        folderPath = os.path.abspath('./A')
        filePaths = [os.path.abspath('./A/Correct Test Name1.txt'),
                     os.path.abspath('./A/Correct Test Name2.txt'),
                     os.path.abspath('./A/Correct Test Name3.txt')]

        os.makedirs(folderPath)
        for p in filePaths:
            os.fdopen(os.open(p, os.O_CREAT)).close()

        file_renamer.run('./testing_script.py', [folderPath], pathsAreDirectories=True)

        self.assertEqual(os.path.isfile(os.path.join(folderPath, "Resulting Name1.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath, "Resulting Name2.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath, "Resulting Name3.txt")), True)

        os.remove(os.path.join(folderPath, "Resulting Name1.txt"))
        os.remove(os.path.join(folderPath, "Resulting Name2.txt"))
        os.remove(os.path.join(folderPath, "Resulting Name3.txt"))
        os.removedirs(folderPath)

    def test_run5_essential(self): # Multiple directories, multiple files
        folderPath1 = os.path.abspath('./A')
        folderPath2 = os.path.abspath('./A/B')
        filePaths = [os.path.abspath('./A/Correct Test Name1.txt'),
                     os.path.abspath('./A/Correct Test Name2.txt'),
                     os.path.abspath('./A/Correct Test Name3.txt'),
                     os.path.abspath('./A/B/Correct Test Name1.txt'),
                     os.path.abspath('./A/B/Correct Test Name2.txt'),
                     os.path.abspath('./A/B/Correct Test Name3.txt')]

        os.makedirs(folderPath1)
        os.makedirs(folderPath2)
        for p in filePaths:
            os.fdopen(os.open(p, os.O_CREAT)).close()

        file_renamer.run('./testing_script.py', [folderPath1, folderPath2],
                         pathsAreDirectories=True)

        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Resulting Name1.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Resulting Name2.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Resulting Name3.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Resulting Name1.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Resulting Name2.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Resulting Name3.txt")), True)

        os.remove(os.path.join(folderPath2, "Resulting Name1.txt"))
        os.remove(os.path.join(folderPath2, "Resulting Name2.txt"))
        os.remove(os.path.join(folderPath2, "Resulting Name3.txt"))
        os.removedirs(folderPath2)
        os.remove(os.path.join(folderPath1, "Resulting Name1.txt"))
        os.remove(os.path.join(folderPath1, "Resulting Name2.txt"))
        os.remove(os.path.join(folderPath1, "Resulting Name3.txt"))
        os.removedirs(folderPath1)

    def test_run6_essential(self): # Run as if ran through command line
        folderPath1 = os.path.abspath('./A')
        folderPath2 = os.path.abspath('./A/B')
        filePaths = [os.path.abspath('./A/Correct Test Name1.txt'),
                     os.path.abspath('./A/Correct Test Name2.txt'),
                     os.path.abspath('./A/Correct Test Name3.txt'),
                     os.path.abspath('./A/B/Correct Test Name1.txt'),
                     os.path.abspath('./A/B/Correct Test Name2.txt'),
                     os.path.abspath('./A/B/Correct Test Name3.txt')]

        os.makedirs(folderPath1)
        os.makedirs(folderPath2)
        for p in filePaths:
            os.fdopen(os.open(p, os.O_CREAT)).close()

        command = "python3 " + os.path.abspath('../file_renamer.py') + " -vvv -d " + os.path.abspath('./testing_script.py') + \
                  " \"" + folderPath1 + "\" " + folderPath2

        os.system(command)

        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Resulting Name1.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Resulting Name2.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Resulting Name3.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Resulting Name1.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Resulting Name2.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Resulting Name3.txt")), True)

        os.remove(os.path.join(folderPath2, "Resulting Name1.txt"))
        os.remove(os.path.join(folderPath2, "Resulting Name2.txt"))
        os.remove(os.path.join(folderPath2, "Resulting Name3.txt"))
        os.removedirs(folderPath2)
        os.remove(os.path.join(folderPath1, "Resulting Name1.txt"))
        os.remove(os.path.join(folderPath1, "Resulting Name2.txt"))
        os.remove(os.path.join(folderPath1, "Resulting Name3.txt"))
        os.removedirs(folderPath1)

    def test_run7_essential(self): # Files that do not match
        folderPath1 = os.path.abspath('./A')
        folderPath2 = os.path.abspath('./A/B')
        filePaths = [os.path.abspath('./A/Incorrect Test Name1.txt'),
                     os.path.abspath('./A/Correct Test Name2.txt'),
                     os.path.abspath('./A/Correct Test Name3.txt'),
                     os.path.abspath('./A/B/Correct Test Name1.txt'),
                     os.path.abspath('./A/B/Incorrect Test Name2.txt'),
                     os.path.abspath('./A/B/Correct Test Name3.txt')]

        os.makedirs(folderPath1)
        os.makedirs(folderPath2)
        for p in filePaths:
            os.fdopen(os.open(p, os.O_CREAT)).close()

        file_renamer.run('./testing_script.py', [folderPath1, folderPath2],
                         pathsAreDirectories=True)

        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Incorrect Test Name1.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Resulting Name2.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Resulting Name3.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Resulting Name1.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Incorrect Test Name2.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Resulting Name3.txt")), True)

        os.remove(os.path.join(folderPath2, "Resulting Name1.txt"))
        os.remove(os.path.join(folderPath2, "Incorrect Test Name2.txt"))
        os.remove(os.path.join(folderPath2, "Resulting Name3.txt"))
        os.removedirs(folderPath2)
        os.remove(os.path.join(folderPath1, "Incorrect Test Name1.txt"))
        os.remove(os.path.join(folderPath1, "Resulting Name2.txt"))
        os.remove(os.path.join(folderPath1, "Resulting Name3.txt"))
        os.removedirs(folderPath1)

    def test_run8_essential(self): # Run as if ran through command line, but only print output
        folderPath1 = os.path.abspath('./A')
        folderPath2 = os.path.abspath('./A/B')
        filePaths = [os.path.abspath('./A/Correct Test Name1.txt'),
                     os.path.abspath('./A/Correct Test Name2.txt'),
                     os.path.abspath('./A/Correct Test Name3.txt'),
                     os.path.abspath('./A/B/Correct Test Name1.txt'),
                     os.path.abspath('./A/B/Correct Test Name2.txt'),
                     os.path.abspath('./A/B/Correct Test Name3.txt')]

        os.makedirs(folderPath1)
        os.makedirs(folderPath2)
        for p in filePaths:
            os.fdopen(os.open(p, os.O_CREAT)).close()

        command = "python3 " + os.path.abspath('../file_renamer.py') + " -p -vvv -d " + os.path.abspath('./testing_script.py') + \
                  " \"" + folderPath1 + "\" " + folderPath2

        os.system(command)

        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Correct Test Name1.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Correct Test Name2.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath1, "Correct Test Name3.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Correct Test Name1.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Correct Test Name2.txt")), True)
        self.assertEqual(os.path.isfile(os.path.join(folderPath2, "Correct Test Name3.txt")), True)

        os.remove(os.path.join(folderPath2, "Correct Test Name1.txt"))
        os.remove(os.path.join(folderPath2, "Correct Test Name2.txt"))
        os.remove(os.path.join(folderPath2, "Correct Test Name3.txt"))
        os.removedirs(folderPath2)
        os.remove(os.path.join(folderPath1, "Correct Test Name1.txt"))
        os.remove(os.path.join(folderPath1, "Correct Test Name2.txt"))
        os.remove(os.path.join(folderPath1, "Correct Test Name3.txt"))
        os.removedirs(folderPath1)