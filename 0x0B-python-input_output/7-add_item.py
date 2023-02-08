#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

try:
    items = load_from_json_file('add_item.json')
except:
    items = []

for arg in sys.argv[1:]:
    items.append(arg)

save_to_json_file(items, 'add_item.json')
