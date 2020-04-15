"""
Renaming script for the Northernlion video series "The Binding of Isaac: AFTERBIRTH+ - Northernlion Plays"

FORMAT IN: {Flavor Text} - The Binding of Isaac{':' or ' - '} AFTERBIRTH+ - Northernlion Plays - Episode {Number}
FORMAT OUT: The Binding of Isaac{':' or ' - '} AFTERBIRTH+ - Northernlion Plays - Episode {####} [{Flavor Text}]
"""

import re


def rename(name):
    search_info = \
        re.compile(r"(?P<path>.*/)?(?P<flavor>.*?)\s\-\s(?P<body>The\sBinding\sof\sIsaac(?:(?:\s\-\s)|(?:\:\s))" +
                   r"AFTERBIRTH\+.*)\s\-\s(?P<episode>Episode\s(?P<episode_number>[0-9]*))(?P<ext>\..*)?", re.I)
    s_obj = re.search(search_info, name)

    if s_obj is None:
        return search_info.pattern, None

    result = (s_obj.groupdict()['path'] if not s_obj.groupdict()['path'] is None else "") + \
             s_obj.groupdict()['body'] + " - " + s_obj.groupdict()['episode'] + " [" + s_obj.groupdict()['flavor'] + \
             "]" + (s_obj.groupdict()['ext'] if not s_obj.groupdict()['ext'] is None else "")

    return search_info.pattern, result
