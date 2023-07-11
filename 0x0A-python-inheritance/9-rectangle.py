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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() and str() representation of Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
