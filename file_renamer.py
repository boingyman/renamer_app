"""

"""
# TODO: New docstring text.
import os
import argparse
import importlib.machinery


def run(scriptPath, filePaths, isPrinting=False):
    scriptPath = os.path.abspath(scriptPath)
    script_module = None

    script_module = importlib.machinery.SourceFileLoader(scriptPath.rsplit('/', 1)[1].rsplit('.', 1)[0],scriptPath).load_module()

    if isPrinting:
        print(script_module.rename(filePaths[0]))
    else:
        os.rename(filePaths[0], script_module.rename(filePaths[0]))


if __name__ == '__main__':
    parsr = argparse.ArgumentParser(description="Surrogate program for renaming files.")
    parsr.add_argument("-s", "--script", action='store', nargs=1, default="",
                       help="The script to import the renaming module. (Required always)")
    parsr.add_argument("-p", "--print", action='store_true',
                       help="Flags the program to print the result instead of renaming the file.")
    parsr.add_argument("location", action='store', nargs=argparse.REMAINDER,
                       help="The target file. (Required, unless '--test-rename' is set)")
    args = vars(parsr.parse_args())

    run(args['script'], args['location'], args['print'])
