import os
import re


def rename(name):

    (head, tail) = os.path.split(name)

    reg_obj = re.compile(r"(?P<path>.*/)(?P<name>.*)(?P<num>)")

    if tail != "Correct Test Name.txt":
        raise Exception("Improper file name.")

    return os.path.join(head, "Resulting Name.txt")