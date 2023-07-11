#!/usr/bin/python3
"""Define JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write object to text file using JSON rep."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
