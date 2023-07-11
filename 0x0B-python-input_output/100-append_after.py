#!/usr/bin/python3
"""define text file"""


def append_after(filename="", search_string="", new_string=""):
    """append text after line

    Args:
        filename (str): name of the file.
        search_string (str): string to search for within the file.
        new_string (str): string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
