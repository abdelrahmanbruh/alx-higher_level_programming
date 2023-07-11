#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves it to a file
"""

import sys
from typing import List
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_item(filename: str, item: str) -> None:
    """
    Adds an item to a list and saves it to a file in JSON format
    """
    try:
        items_list = load_from_json_file(filename)
    except FileNotFoundError:
        items_list = []
    items_list.append(item)
    save_to_json_file(items_list, filename)

if __name__ == "__main__":
    filename = "add_item.json"
    items = sys.argv[1:]
    for item in items:
        add_item(filename, item) 
