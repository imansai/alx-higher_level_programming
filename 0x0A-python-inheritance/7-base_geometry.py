#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsents base geometry."""

    def area(self):
        """Area not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Confirms if parameter is an integer.

        Args:
            name (str): The parameter name.
            value (int): The parameter to confirm.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
