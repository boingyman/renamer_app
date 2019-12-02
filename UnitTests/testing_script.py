import os


def rename(name) -> str:

    (head, tail) = os.path.split(name)

    if tail != "Correct Test Name.txt":
        raise Exception("Improper file name.")

    return os.path.join(head, "Resulting Name.txt")