## Changelog

##### Planned

* Added ability to use multiple script files.
* Added ability to recursively go through subdirectories of given directories.
* Made the script API more unified to the main application.

#### v3.0.0 [2020-4-14]

* Changed API for script files.
    * `rename(`

#### v2.1.0 [2020-4-14]

* Added flag `-v` and `--verbose` for more detailed output.

#### v2.0.1 [2020-4-12]

* Minor changes to various files.
    * `file_renamer.py`:
        * Formatting and comments.
    * `isaacpost1424.py`:
        * Formatting.
    * `dcimdatetime.py`:
        * Formatting.
    * `testing_script.py`:
        * Formatting.

#### v2.0.0 [2020-4-12]

* Changed compatible Python version in `readme.md` to 3.7+.
* Added ability to rename multiple individual files.
    * Changed argument order. Previously, format was `file_renamer.py -s script_file.py [-d] 
    [-p] file_to_rename.ext`. Format is now `file_renamer.py [-d] [-p] script_file.py 
    file_to_rename.ext ...`.
    * If given file does name match the required format of the script file, the file will 
    be skipped and execution will continue.
* Added ability to rename multiple files inside a given directory.
    * If a file contained within the directory does not match the required format of the 
    script file, the file will be skipped and execution will continue.
    * Added appropriate unit test cases.
* Made changes to help descriptions for consistency.
* Changes to `dcimdatetime.py`:
    * Added ability to capture prefix text, as some devices prefix text before the given 
    timestamp name.
    * Clarified description.
* Various changes to `API.md`.

#### v1.2.0 [2020-4-7]

* Changed descriptions to better represent the functionality and use of the script.
* Changes to `isaacpost1424.py`:
    * Changed descriptions to better represent the functionality and use of the 
    script.
* Added `dcimdatetime.py`.
* Added unit test `test_dcimdatetime`.

#### v1.1.0 [2019-12-2]

* Added `readme.md`.
* Added `renaming_exceptions.py`.
    * Includes the exception class `InvalidFileNameError`
* Removed flags `-r` and `--rename`.
    * Renaming files is now default behavior without flags.
* Removed flags `-i` and `--ignore-errors`.
    * Feature removed entirely.
* Removed flags `-t` and `--test-rename`.
    * Feature removed entirely.
* Changes to `isaacpost1424.py`:
    * Removed `test_string` method.
* Added unit tests, including the files:
    * `test_file_renamer.py`
    * `test_isaacpost1424.py`
    * `testing_script.py`

##### v1.0.0 [2019-11-23]

- Initial release.
- Includes `isaacpost1424.py`.