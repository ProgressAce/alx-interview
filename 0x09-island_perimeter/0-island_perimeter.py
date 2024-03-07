#!/usr/bin/python3
"""Calculates an island's perimeter."""


def island_perimeter(grid):
    """Computes the island perimeter according to a 2D matrix.

    Arg:
        grid(list of lists of ints): a 2D matrix of 0s and 1s.

    <grid> is rectangular, with a width and height that should not exceed 100.
    <grid> is completely surrounded by water. ** Therefore, no need to worry
    about surpassing outer edge of matrix.

    Returns:
        the island's perimeter."""

    # the bun and neatly placed wrapping - protection
    if (not isinstance(grid, list) or not isinstance(grid[0], list)
            or not isinstance(grid[0][0], int)):
        return "TypeError: grid is not a list of lists of ints. `~`"

    grid_height = len(grid)
    grid_width = len(grid[0])
    grid_perimeter = (grid_height * 2) + (grid_width * 2)

    # ensure grid's width and height does not exceed 100
    if grid_perimeter > 100:
        raise ValueError("grid's width and height should not exceed 100")

    # the meat, (the taste and sustenance/nutrition) - the operations
    perimeter = 0
    for i in range(grid_height):
        for j in range(grid_width):
            # a piece of land (island block) was found
            if grid[i][j] == 1:
                perimeter += 4

                # check for land to one left of island block
                if grid[i][j - 1] == 1:
                    perimeter -= 1

                # check for land to one up of island block
                if grid[i - 1][j] == 1:
                    perimeter -= 1

                # check for land to one right of island block
                if grid[i][j + 1] == 1:
                    perimeter -= 1

                # check for land to one down of island block
                if grid[i + 1][j] == 1:
                    perimeter -= 1

            else:
                continue

    return perimeter
