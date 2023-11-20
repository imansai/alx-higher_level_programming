#!/usr/bin/python3
"""Defines a function that converts text to json."""
import json


def to_json_string(my_obj):
    """Returns JSON representation of a string"""
    return json.dumps(my_obj)
