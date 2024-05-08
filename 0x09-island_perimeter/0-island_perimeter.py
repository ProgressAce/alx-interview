#!/usr/bin/python3
"""Solves the perimeter of the island."""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island given as a 2D grid.

    Arg:
        grid(list): a list of lists of integers, representing water and land.
    Returns:
        the calculated perimeter of the island.
    """

    # existing_island = 0 to ensure only one island exists on grid
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not grid[i][j]:
                continue

            # the current cell is one beyond this point

            if i != 0:
                if grid[i - 1][j] == 0:
                    perimeter += 1

            if j != 0:
                if grid[i][j - 1] == 0:
                    perimeter += 1

            if i < len(grid[0]) - 1:
                if grid[i + 1][j] == 0:
                    perimeter += 1

            if j < len(grid[0]) - 1:
                if grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
