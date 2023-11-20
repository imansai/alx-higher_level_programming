#!/usr/bin/python3
"""Defines a function that converts JSON to object."""
import json


def from_json_string(my_str):
    """Returns object representation of a JSON."""
    return json.loads(my_str)
