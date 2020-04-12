### API Information

##### file_renamer.run(scriptPath, filePaths, pathsAreDirectories=False, isPrinting=False)

(found in `file_renamer.py`)

Arguments:
* `scriptPath` - The Path to the script that the application will import.<br>
* `filePaths` - An array of strings that each represents a path to a target file.<br>
* `pathsAreDirectories` - Indicates whether the given file paths should be treated as
directories as opposed to files.
* `isPrinting` - Indicates whether the program should output the result to stdout or 
rename the given file(s).

Method does not return a result. Depending on `isPrinting`, the method will either print to
stdout or rename the given file(s) in `filePaths`, both based on the `rename(name)` function
found in the script given by `scriptPath`.

---

##### {scriptname}.rename(name)

Arguments:
* `name` - The given name or path.

Method returns a string that is the modified result of `name`. If `name` is a file path, the
method must return the given directory and given extension as well.

The following exceptions should be thrown if invalid input is given:
* `InvalidFileNameError` - Occurs when the given `name` argument is determined to be invalid
and cannot be renamed.