#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
BaseGeometry
"""


class Square(Rectangle):
    """BaseGeometry"""

    def __init__(self, size):
        """Method for attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2
