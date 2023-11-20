#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """This function divides each element within a matrix.

    Args:
        matrix (list): A list consisting of integers or floats.
        div (int/float): The number used as the divisor.
    Raises:
        TypeError: If the matrix contains elements that are not numeric.
        TypeError: If the matrix contains rows with varying lengths.
        TypeError: If div is not of type int or float.
        ZeroDivisionError: If div is set to zero.
    Returns:
        A new matrix depicting the outcome of the division operation.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
