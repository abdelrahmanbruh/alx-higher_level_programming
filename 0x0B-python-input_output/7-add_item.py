#!/usr/bin/python3
"""define le add"""
import json


def save_to_json_file(my_obj, filename):
    """wadshada"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
