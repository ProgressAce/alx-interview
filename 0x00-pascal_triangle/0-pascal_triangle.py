#!/usr/bin/python3
"""Defines a function for representing Pascal's triangle."""

from math import factorial


def pascal_triangle(n):
    """Returns a list of lists of integers, representing the triangle.

    Assumes n will always be an integer.
    Return:
        an empty list if n < 0."""
    row = 1
    triangle = []

    while row <= n:
        tri_lst = []
        for col in range(row):
            if col in (0, row - 1):  # check for first or last element of row
                tri_lst.append(1)
            else:
                # formula for any entry in the pascal triangle
                # row! / column!(row - column)!
                # row and column indexing should begin at 0.
                pascal_entry = factorial(row - 1) / (
                    factorial(col) * factorial(row - 1 - col)
                )
                tri_lst.append(round(pascal_entry))

        row += 1
        triangle.append(tri_lst)

    return triangle
