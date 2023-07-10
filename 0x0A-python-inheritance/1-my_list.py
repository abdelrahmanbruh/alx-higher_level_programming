#!/usr/bin/python3
"""My list"""


class MyList(list):
    """my list"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
