#!/usr/bin/python3
"""BaseGeometry."""


class BaseGeometry:
    """base geometry."""

    def area(self):
        """area not impmlem,eted"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a param as int

        Args:
            name (str): name of the parameter.
            value (int): parameter to validate
        Raises:
            TypeError: If value is not integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
