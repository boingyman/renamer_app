import re


def rename(name):
    search_info = re.compile(r"(?P<path>.*/)?(?P<name>Correct\sTest\sName)(?P<num>\d*)(?P<ext>\.txt)?")
    s_obj = re.search(search_info, name)

    if s_obj is None:
        return search_info.pattern, None

    result = (s_obj.groupdict()['path'] if not s_obj.groupdict()['path'] is None else "") + \
             "Resulting Name" + s_obj.groupdict()['num'] + \
             (s_obj.groupdict()['ext'] if not s_obj.groupdict()['ext'] is None else "")

    return search_info.pattern, result
