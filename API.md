### API Information

##### file_renamer.run(scriptPath, filePaths, isPrinting = False)

(found in `file_renamer.py`)

Arguments:
* `scriptPath` - The Path to the script that the application will import.<br>
* `filePaths` - An array of strings that each represents a path to a target file.<br>
* `isPrinting` - Indicates whether the program should output the result to stdout or 
rename the given file(s).

Method does not return a result. Depending on `isPrinting`, the method will either print to
stdout or rename the given file(s) in `filePaths`, both based on the `rename(name)` function
found in the script given by `scriptPath`.

The following exceptions can be thrown if invalid inputs are given:
* `FileNotFoundError` - Occurs when the given file paths do not point to an existing file.
* `AttributeError` - Occurs when giving a script file path that points to a file that does
not have the method `rename()`.
* `TypeError` - Occurs when passing an object of unexpected type.

---

##### {scriptname}.rename(name)

Arguments:
* `name` - The given name or path.

Method returns a string that is the modified result of `name`. If `name` is a file path, the
method must return the given directory and given extension as well.

The following exceptions can be thrown if invalid input is given:
* `InvalidFileNameError` - Occurs when the given `name` argument is determined to be invalid
and cannot be renamed.
* `TypeError` - Occurs when passing an object of unexpected type.