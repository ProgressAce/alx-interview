#!/usr/bin/python3
"""Defines a function for representing Pascal's triangle."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers, representing the triangle.

    Assumes n will always be an integer.

    Args:
    n (integer): The number of rows to create for Pascal's Triangle.

    Returns:
    An empty list if n <= 0
    """
    if n <= 0:
        return []

    row = 1
    triangle = []

    while row <= n:
        tri_lst = []
        for col in range(row):
            if col in (0, row - 1):  # check for first and last element of row
                tri_lst.append(1)
            else:
                # add new entry based on the sum of its two upper elements
                # row - 2 is used since row starts at 1 and not 0
                pas_entry = triangle[row - 2][col - 1] + triangle[row - 2][col]
                tri_lst.append(pas_entry)

        row += 1
        triangle.append(tri_lst)

    return triangle
