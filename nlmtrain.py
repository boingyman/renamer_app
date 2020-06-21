"""
Renaming script for the Northernlion video series "Monster Train"

FORMAT IN: {Flavor Text} _ Monster Train (Episode {Number})
FORMAT OUT: Monster Train - Episode {Number} - {Flavor Text}
"""

import re


def rename(name):
    search_info = \
        re.compile(r"(?P<path>.*/)?(?P<flavor>.*?)\s\_\s(?P<body>Monster\sTrain)\s\((?P<episode>Episode\s(?P<episode_number>[0-9]*))\)(?P<ext>\..*)?", re.I)
    s_obj = re.search(search_info, name)

    if s_obj is None:
        return search_info.pattern, None

    result = (s_obj.groupdict()['path'] if not s_obj.groupdict()['path'] is None else "") + \
             s_obj.groupdict()['body'] + " - " + s_obj.groupdict()['episode'] + " - " + s_obj.groupdict()['flavor'] + \
             (s_obj.groupdict()['ext'] if not s_obj.groupdict()['ext'] is None else "")

    return search_info.pattern, result
