#!/usr/bin/python3
"""Define text file-reading function"""


def read_file(filename=""):
    """print contents of a UTF8 text file to the stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
