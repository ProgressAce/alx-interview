#!/usr/bin/python3
"""Program that gives all the valid solutions to the n queen problem."""

from sys import argv


def is_safe(board, row, col):
    """Checks if the board position is safe from any other queen attacks.

    Args:
        board(list of lists): the chess board of a certain size.
        row(int): the row position to check for safety.
        col(int): the column position to check for safety.

    Returns:
        True is it is safe, False if the position can be attacked."""

    board_len = len(board)

    # check possible horizontal attacking positions (queen already placed)
    for x in range(board_len):
        if board[row][x] == "Q":
            return False

    # check possible vertical attacking positions (queen already placed)
    for y in range(board_len):
        if board[y][col] == "Q":
            return False

    # check for existing queen placement in the upper left diagonal
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == "Q":
            return False

    # check for existing queen placement in the upper right diagonal
    for r, c in zip(range(row, -1, -1), range(col, board_len)):
        if board[r][c] == "Q":
            return False

    # check for existing queen placement in the lower left diagonal
    for r, c in zip(range(row, board_len), range(col, -1, -1)):
        if board[r][c] == "Q":
            return False

    # check for existing queen placement in the lower right diagonal
    for r, c in zip(range(row, board_len), range(col, board_len)):
        if board[r][c] == "Q":
            return False

    return True


def print_board_solution(board):
    """Prints all the queen positions of the given board's nqueen solution."""

    board_len = len(board)
    positions = []

    for i in range(board_len):
        for j in range(board_len):
            if board[i][j] == "Q":
                positions.append([i, j])

    print(positions)


def solve_n_queen(board, col):
    """
    Looks at all the possible positions to put n queens on the board.
    and chooses all the valid positions.
    """

    board_len = len(board)

    if col == board_len:
        print_board_solution(board)
        return

    for row_idx in range(board_len):

        if is_safe(board, row_idx, col):
            board[row_idx][col] = "Q"

            solve_n_queen(board, col + 1)

            board[row_idx][col] = "."


def main():
    """Entry point of the program.

    Parses the argument of the program and uses it as the <n> input
    for the 'n queens problem.'The goal is to place n queens on a nxn board
    each queen in a safe position, not being able to attack another nor be
    attacked.

    The program works out all the valid solutions for the problem
    and returns all the queen positions for each solution of '<n> queens'.

    Use:
        ./n-queen <n>
    """

    # program's argument validations
    arg_count = len(argv) - 1
    if arg_count != 1:
        print("Usage: nqueens N")
        exit(1)

    n = argv[1]

    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [["." for block in range(n)] for row in range(n)]

    solve_n_queen(board, 0)


if __name__ == "__main__":
    main()
