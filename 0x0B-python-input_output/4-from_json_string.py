#!/usr/bin/python3
 """this code returns the Python object representation of a JSON string"""

import json


def from_json_string(my_str):
    return json.loads(my_str)
