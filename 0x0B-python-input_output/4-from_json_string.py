#!/usr/bin/python3
"""define JSON-to-object function."""
import json


def from_json_string(my_str):
    """return Python object representation of a JSON string."""
    return json.loads(my_str)
