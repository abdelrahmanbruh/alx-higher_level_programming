#!/usr/bin/python3
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, 'add_item.json') 

loaded_list = load_from_json_file('add_item.json')

print(my_list)
print(loaded_list)
