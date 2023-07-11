#!/usr/bin/python3
"""define python class to a JSON function."""


def class_to_json(obj):
    """Return the dictionary of a simple data struct"""
    return obj.__dict__
