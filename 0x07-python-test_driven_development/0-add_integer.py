#!/usr/bin/python3
"""Defines function that adds two integers."""


def add_integer(a, b=98):
    """Returns the sum of a and b.

    Float are typecasted to integers before addition.

    Raises:
        TypeError: If a or b is not an integer nor a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
