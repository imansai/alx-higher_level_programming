#!/usr/bin/python3
"""Defines a function that evaluates classes."""


def is_same_class(obj, a_class):
    """Checks if object is exactly an instance of a specified class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to be matched to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
