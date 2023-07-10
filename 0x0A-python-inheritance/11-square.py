#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
BaseGeometry
"""


class Square(Rectangle):
    """asdaf"""

    def __init__(self, size):
        """Method for attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)