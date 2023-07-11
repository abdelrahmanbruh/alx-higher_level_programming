#!/usr/bin/python3
"""defines a student class"""


class Student:
    """represent a student."""

    def __init__(self, first_name, last_name, age):
        """initialize new Student.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dictionary rep of the Student."""
        return self.__dict__
