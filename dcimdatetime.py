"""
Photos from devices, such as Android mobile devices, may place photos/videos into a DCIM folder with a date/time format
of when it was captured. It is not very readable as the digits are only separated between the date and time of day. Note
that this is not a standardized format, which may vary between devices or manufacturers of said devices.

FORMAT IN: {Year}{Month}{Day}_{Hours}{Minutes}{Seconds}{Left Over Text}
FORMAT OUT: {Year} {Month} {Day} - {Hours}_{Minutes}_{Seconds}{Left Over Text}
"""

import re


def rename(name):
    search_info = re.compile(r"(?P<path>.*/)?(?P<prefixtext>.*)(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})_" +
                             r"(?P<hours>\d{2})(?P<minutes>\d{2})(?P<seconds>\d{2})(?P<extra>.*)(?P<ext>\..*)?", re.I)
    s_obj = re.search(search_info, name)

    if s_obj is None:
        return search_info.pattern, None

    result = (s_obj.groupdict()['path'] if not s_obj.groupdict()['path'] is None else "") + \
             s_obj.groupdict()['prefixtext'] + s_obj.groupdict()['year'] + " " + s_obj.groupdict()['month'] + " " + \
             s_obj.groupdict()['day'] + " - " + s_obj.groupdict()['hours'] + "_" + s_obj.groupdict()['minutes'] + \
             "_" + s_obj.groupdict()['seconds'] + s_obj.groupdict()['extra'] + \
             (s_obj.groupdict()['ext'] if not s_obj.groupdict()['ext'] is None else "")

    return search_info.pattern, result
