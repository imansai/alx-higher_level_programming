#!/usr/bin/python3
"""Defines Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initializes new square.

        Args:
            size (int): The new square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
