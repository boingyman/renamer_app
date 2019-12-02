## Changelog

##### Planned

* Added feature to rename multiple individual files.
* Changed descriptions to better represent the functionality and use of the script.
* Changes to `isaacpost1424.py`:
    * Changed descriptions to better represent the functionality and use of the 
    script.

#### v1.1.0 []

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