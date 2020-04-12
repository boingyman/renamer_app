"""
Renames given files, or files inside given directories, using a .py script given as a string argument.
"""
import os
import argparse
import importlib.machinery
from renaming_exceptions import *


def run(scriptPath, filePaths, pathsAreDirectories=False, isPrinting=False):
    def do_rename(fileList):
        for file in fileList:
            if not os.path.isfile(file):
                next
            try:
                if isPrinting:
                    print(script_module.rename(file))
                else:
                    os.rename(file, script_module.rename(file))
            except InvalidFileNameError as err:
                next

    # Load the script module from a given path
    scriptPath = os.path.abspath(scriptPath)
    script_module = importlib.machinery.SourceFileLoader(scriptPath.rsplit('/', 1)[1].rsplit('.', 1)[0],
                                                         scriptPath).load_module()

    if pathsAreDirectories:
        # Make a list of files from all directories
        files = []
        for dir in filePaths:
            if not os.path.isdir(dir):
                next

            filesInDirectory = []
            for f in os.listdir(dir):
                if os.path.isfile(os.path.join(dir, f)):
                    filesInDirectory.append(f)

            if len(filesInDirectory) == 0:
                print("Directory `" + dir + "`" + "does not contain any files, skipping...")
            else:
                for f in filesInDirectory:
                    files.append(os.path.join(dir, f))

        do_rename(files)
    else:
        do_rename(filePaths)


if __name__ == '__main__':
    parsr = argparse.ArgumentParser(description="Surrogate program for renaming files.")
    parsr.add_argument("-p", "--print", action='store_true',
                       help="print the results instead of renaming files")
    parsr.add_argument("-d", "--directories", action='store_true',
                       help="indicates that the given target paths are to directories instead of specific files")
    parsr.add_argument("files", action='store', nargs=argparse.REMAINDER,
                       help="the script and target files/folders; script will always be given first")
    args = vars(parsr.parse_args())

    run(args['files'][0], args['files'][1::], args['directories'], args['print'])
