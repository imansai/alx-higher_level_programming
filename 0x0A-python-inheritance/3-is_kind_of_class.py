#!/usr/bin/python3
"""Defines a class and inheritance class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to be matched.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
