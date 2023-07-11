#!/usr/bin/python3
"""Defines an inherited list class."""


class MyList(list):
    """Implements sorted printing for list class."""

    def print_sorted(self):
        """Prints list in sorted ascending order."""
        print(sorted(self))
