#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns object's available attributes list."""
    return (dir(obj))
