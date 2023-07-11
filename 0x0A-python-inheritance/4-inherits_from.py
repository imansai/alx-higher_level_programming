#!/usr/bin/python3
"""Defines inherited class-checker function."""


def inherits_from(obj, a_class):
    """Checks if object is inherited instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to be matched.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
