## Readme

#### Description
`file_renamer.py` is a script that is able to rename files through the use of other
scripts through a dead simple API. Essentially, this allows for an easier to
maintain library of scripts that contain solely the functionality of returning a
new name based on the input.

The API contains one requirement: the definition of the function `rename` in the
module that accepts an input string (typically a file path) and outputs a string.
Users are able to create their own scripts following this simple API.

#### Requirements
* Linux based system - Assumed incompatibility with other platforms due to lack 
of testing.
* Python 3.6+

#### TL:DR
Script can rename files by importing other scripts at runtime.
User can create their own script following a simple API.

#### Note on code maintenance
This is not dedicated project. Do not expect updates to come out on a timely
basis, nor expect the repository owner to be available.
