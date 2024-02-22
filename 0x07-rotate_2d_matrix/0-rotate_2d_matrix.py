#!/usr/bin/python3
"""Module for rotating a 2D matrix 90 degrees in a clockwise-direction."""


def rotate_matrix(matrix: list):
    """Rotates the matrix in a 90 degrees clockwise-direction.

       The rotation happens in-place (without creating a duplicate).
       Assumes that the matrix is a 2 dimensional list of size nxn.
       Arg:
           matrix: the 2D list of lists.
    """

    matrix_len = len(matrix)

    # swap along the main left diagonal elements
    for i in range(matrix_len):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(matrix_len):
        for j in range(int(matrix_len / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][matrix_len - j - 1]
            matrix[i][matrix_len - j - 1] = temp


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(matrix)
    rotate_matrix(matrix)
    print("90 degrees rotation")
    for row in matrix:
        print(row)
