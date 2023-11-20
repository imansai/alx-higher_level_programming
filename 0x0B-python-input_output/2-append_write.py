#!/usr/bin/python3
"""Defines function that appends a string to a file."""


def append_write(filename="", text=""):
    """Adds a string at the end of a UTF8 text file.

    Args:
        filename (str): Filename to append to.
        text (str): String to be appended.
    Returns:
        Number of appended characters.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
