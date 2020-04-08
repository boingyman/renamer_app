"""
Renaming script for the Northernlion video series "The Binding of Isaac: AFTERBIRTH+ - Northernlion Plays"

FORMAT IN: {Flavor Text} - The Binding of Isaac{':' or ' - '} AFTERBIRTH+ - Northernlion Plays - Episode {Number}
FORMAT OUT: The Binding of Isaac{':' or ' - '} AFTERBIRTH+ - Northernlion Plays - Episode {####} [{Flavor Text}]
"""

import re
from renaming_exceptions import *


def rename(name):

    search_pattern = re.compile(r"(?P<path>.*/)?(?P<flavor>.*?)\s\-\s(?P<body>The\sBinding\sof\sIsaac(?:(?:\s\-\s)|(?:\:\s))" + \
                                r"AFTERBIRTH\+.*)\s\-\s(?P<episode>Episode\s(?P<episode_number>[0-9]*))(?P<ext>\..*)?", re.I)
    s_obj = re.search(search_pattern, name)

    result = ""

    if s_obj is None:
        raise InvalidFileNameError("Given file name did not match regex pattern:\n" + search_pattern.pattern + "\n")

    result = s_obj.groupdict()['body'] + " - " + s_obj.groupdict()['episode'] + " [" + s_obj.groupdict()['flavor'] + "]"

    # Checks for 'ext' capture group, as it is the file extension, if it exists.
    if not s_obj.groupdict()['ext'] is None:
        result = result + s_obj.groupdict()['ext']

    # Checks for 'path' capture group, as it is the path to the file, if it exists.
    if not s_obj.groupdict()['path'] is None:
        result = s_obj.groupdict()['path'] + result

    return result
