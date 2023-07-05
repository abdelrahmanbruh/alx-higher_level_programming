#!/usr/bin/python3
"""make a locked class"""


class LockedClass:
    """
    A Locked Class

    Attributes:
        first_name (str): first name.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """create a new locked class """

        self.first_name = "first_name"
