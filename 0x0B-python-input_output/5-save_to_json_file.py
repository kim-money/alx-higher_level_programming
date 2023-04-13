#!/usr/bin/python3
"""This module defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as fel:
        json.dump(my_obj, fel)
