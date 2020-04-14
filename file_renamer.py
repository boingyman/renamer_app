"""
Renames given files, or files inside given directories, using a .py script given as a string argument.
"""
import os
import argparse
import importlib.machinery
from renaming_exceptions import *

verbosity = 0

def verbose_print(requiredVerbosityLevel, message):
    if verbosity >= requiredVerbosityLevel:
        print(message)

def run(scriptPath, filePaths, pathsAreDirectories=False, isPrinting=False):
    def do_rename(fileList):
        verbose_print(2, "Starting renaming of files...")
        for file in fileList:
            if not os.path.isfile(file):
                next

            verbose_print(3, file + "  ->  " + script_module.rename(file))
            if isPrinting:
                print(script_module.rename(file))
            else:
                try:
                    os.rename(file, script_module.rename(file))
                except InvalidFileNameError as err:
                    verbose_print(1, "File `" + file + "` did not match expected file format. File has been skipped.")
                    next
                except:
                    next

    # Load the script module from a given path
    scriptPath = os.path.abspath(scriptPath)
    verbose_print(2, "Loading script from path: " + scriptPath)
    script_module = importlib.machinery.SourceFileLoader(scriptPath.rsplit('/', 1)[1].rsplit('.', 1)[0],
                                                         scriptPath).load_module()

    if pathsAreDirectories:

        # Make a list of files from all directories
        files = []
        for dir in filePaths:
            verbose_print(1, "Starting search in directory: " + dir)
            if not os.path.isdir(dir):
                next

            filesInDirectory = []
            for f in os.listdir(dir):
                if os.path.isfile(os.path.join(dir, f)):
                    verbose_print(3, "Located file: " + f)
                    filesInDirectory.append(f)

            verbose_print(1, "Found " + str(len(filesInDirectory)) + " files in directory.")

            files.extend(os.path.join(dir, f) for f in filesInDirectory)

        do_rename(files)
    else:
        do_rename(filePaths)


if __name__ == '__main__':
    parsr = argparse.ArgumentParser(description="Surrogate program for renaming files.")
    parsr.add_argument("-p", "--print", action='store_true',
                       help="print the results instead of renaming files")
    parsr.add_argument("-v", "--verbose", action='count', default=0,
                       help="enables debug information")
    parsr.add_argument("-d", "--directories", action='store_true',
                       help="indicates that the given target paths are to directories instead of specific files")
    parsr.add_argument("files", action='store', nargs=argparse.REMAINDER,
                       help="the script and target files/folders; script will always be given first")
    args = vars(parsr.parse_args())

    verbosity = 1#args['verbose']

    verbose_print(2, "---file_renamer.py---\n" +
                     "*Argument values:*\n" +
                     ''.join([str(a) + " :: " + str(args[a]) + "\n" for a in args]) +
                     "\nRunning main program...")

    run(args['files'][0], args['files'][1::], args['directories'], args['print'])

    verbose_print(2, "Execution has finished.")
