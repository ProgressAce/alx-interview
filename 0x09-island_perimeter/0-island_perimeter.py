#!/usr/bin/python3
""" Solves the island perimeter problem.
"""


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid:

    Expectations:
    grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected to
    the water surrounding the island).

    """
    if not grid:
        return -1

    grid_height = len(grid)
    grid_width = len(grid[0])

    if grid_height > 100 or grid_width > 100:
        return -1

    perimeter = 0
    for i in range(grid_height):
        for j in range(grid_width):
            if grid[i][j] == 1:
                perimeter += 4

                if j - 1 != -1:
                    # checks for left island cell
                    if grid[i][j - 1] == 1:
                        perimeter -= 1

                if i + 1 != grid_height:
                    # checks for bottom island cell
                    if grid[i + 1][j] == 1:
                        perimeter -= 1

                if j + 1 != grid_width:
                    # checks for right island cell
                    if grid[i][j + 1] == 1:
                        perimeter -= 1

                if i - 1 != -1:
                    # checks for top island cell
                    if grid[i - 1][j] == 1:
                        perimeter -= 1

    return perimeter
