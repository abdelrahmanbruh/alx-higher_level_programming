#!/usr/bin/python3
"""define string-to-JSON function."""
import json


def to_json_string(my_obj):
    """return JSON representation of string object."""
    return json.dumps(my_obj)
