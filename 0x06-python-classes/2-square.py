#!/usr/bin/python3
"""Defining empty class Square."""


class Square:
    """Defining square."""

    def __init__(self, size=0):
        """Initializing new Square.

        Args:
            size (int): New square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
