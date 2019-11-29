"""
Program for batch renaming files.

SUPPORTS: Any file type with a name following the 'FORMAT IN' expected format.
RESULTS: Run with flag '--show-outcomes' for more details.
"""

import os
import argparse
import importlib.machinery


parsr = argparse.ArgumentParser(description="Surrogate program for renaming files.")
parsr.add_argument("-o", "--show-outcomes", action='store_true', help="Makes the program only explain what the program does when given certain flags.")
parsr.add_argument("-s", "--script", action='store', nargs=1, default="", help="The script to import the renaming module. (Required always)")
parsr.add_argument("-r", "--rename", action='store_true', help="Flags the program to rename the file. (Required choice)")
parsr.add_argument("-p", "--print", action='store_true', help="Flags the program to print the result. (Required choice)")
parsr.add_argument("-t", "--test-rename", action='store_true', help="Creates a dummy file in the same directory and renames it. (Requires '--rename')")
parsr.add_argument("-i", "--ignore-errors", action='store_true', help="When encountering certain exceptions, program will fail silently")
parsr.add_argument("location", action='store', nargs=argparse.REMAINDER, help="The target file. (Required, unless '--test-rename' is set)")
args = vars(parsr.parse_args())

if args['show_outcomes']:
    print("When using the '-r' or '--rename' flag, the program will rename the file that is given by the user.")
    print("When using the '-p' or '--print' flag, the program will print the full path with the modified file name.")
    print("Both flags are meant to be used separate from each other. Signalling both/none will result in an error and")
    print("\tprogram execution will be terminated.")
    print()
    print("This program relies on dynamically imported python scripts to access two functions, 'rename' and 'test_string'.")
    print("The method 'rename' must have the signature 'rename(str) -> str'.")
    print("The method 'test_string' will have the signature 'test_string() -> str'.")
    print("'rename' will perform the renaming of a valid given string and 'test_string' will provide a sample of a valid string to fulfil the purpose of the '--test-rename' flag.")
    print()
    print("'--test-rename' will create a file in the current directory and then immediately rename it.")
    exit(0)


script_module = None

if args['script'] == "" or not os.path.isfile(args['script'][0]):
    raise Exception("Script file path must be to a file.")
else:
    try:
        script_module = importlib.machinery.SourceFileLoader(args['script'][0].rsplit('/', 1)[1].rsplit('.', 1)[0], args['script'][0]).load_module()
    except:
        if args['ignore_errors']:
            pass
        else:
            raise Exception("Invalid script file path.")

if args['rename'] and args['print']:
    if args['ignore_errors']:
        pass
    else:
        raise Exception("'--rename' and '--print' may not be used at the same time.")
if args['rename'] and args['print']:
    if args['ignore_errors']:
        pass
    else:
        raise Exception("'--rename' or '--print' are required to be specified.")


if args['rename']:
    if args['test_rename']:
        test_file_path = os.getcwd() + "/" + script_module.test_string()
        open(test_file_path, 'w+').close()
        os.rename(test_file_path, script_module.rename(test_file_path))
    else:
        try:
            os.rename(args['location'][0], script_module.rename(args['location'][0]))
        except Exception:
            pass
else:
    try:
        print(script_module.rename(args['location'][0]))
    except Exception:
        pass