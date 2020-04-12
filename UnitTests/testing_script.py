import os
import re
from renaming_exceptions import *


def rename(name):
    search_pattern = re.compile(r"(?P<path>.*/)?(?P<name>Correct\sTest\sName)(?P<num>\d*)(?P<ext>\.txt)?")
    s_obj = re.search(search_pattern, name)

    result = ""

    if s_obj is None:
        raise InvalidFileNameError("Given file name did not match regex pattern:\n" + search_pattern.pattern + "\n")

    result = "Resulting Name" + s_obj.groupdict()['num']

    # Checks for 'ext' capture group, as it is the file extension, if it exists.
    if not s_obj.groupdict()['ext'] is None:
        result = result + s_obj.groupdict()['ext']

    # Checks for 'path' capture group, as it is the path to the file, if it exists.
    if not s_obj.groupdict()['path'] is None:
        result = s_obj.groupdict()['path'] + result

    return result
