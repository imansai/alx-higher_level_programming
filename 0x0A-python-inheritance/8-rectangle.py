#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializes new Rectangle.

        Args:
            width (int): The new Rectangle width.
            height (int): The new Rectangle height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
