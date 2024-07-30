#!/usr/bin/python3
"""
0-main: use case of <island_perimeter> function
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

    grid2 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid2))

    grid3 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid3))

# might have this scenario instead of assuming not to get this scenario of diagonal cells
    grid4 = [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    # 8, since island cells are assumed to only be connected horizontally & vertically.
    print(island_perimeter(grid4))

    grid5 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    #
    # TODO: ValueError, since grid's rectangular height and width are assumed to not exceed 100
    try:
        print(island_perimeter(grid5))  # prints 12
    except ValueError:
        print("ValueError caught!")

    grid6 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0]
    ]
    # list IndexError as island cells are assumed to be completely surrounded by water (0s).
    try:
        print(island_perimeter(grid6))
    except IndexError:
        print("IndexError caught!")

    grid7 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]
    # list IndexError as island cells are assumed to be completely surrounded by water (0s).
    try:
        print(island_perimeter(grid7))
    except IndexError:
        print("IndexError caught!")

    grid8 = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    # list IndexError as island cells are assumed to be completely surrounded by water (0s).
    try:
        print(island_perimeter(grid8))
    except IndexError:
        print("IndexError caught!")

    grid9 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    # 8, since island cells are assumed to only be connected horizontally & vertically.
    print(island_perimeter(grid9))
