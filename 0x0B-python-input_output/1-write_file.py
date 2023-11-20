#!/usr/bin/python3
"""Defines a function that writes into files."""


def write_file(filename="", text=""):
    """Writes a text in UTF8 text file.

    Args:
        filename (str): Filename to write in.
        text (str): Text to be written.
    Returns:
        Number of written characters.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
