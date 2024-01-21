#!/usr/bin/python3
"""Defines a function to determine the fewest operations to solve the issue"""

from typing import List


def minOperations(n: int) -> int:
    """Calculates the fewest number of operations needed to get exactly
    n H characters in a file.

    Returns:
        the minimum number of operations,
        or 0 if it is impossible to achieve."""

    if n <= 1 or not isinstance(n, int):
        return 0

    op_count: int = 0
    file_text: str = "H"
    clipboard: str = ""

    # choosing factors of n and their factors to calculate minimum
    # operation count
    prime_factor: int = 1
    chosen_factor: int = 1
    p_factors: List[int] = []

    # improve my using a dict of key/value pairs for chosen_factors
    # & prime_factors

    # find second biggest factor of n.
    for factor in range(2, int(n / 2)):
        if n % factor == 0:
            chosen_factor = n / factor
            prime_factor = factor

            p_factors.append(prime_factor)
            break

    # this means that n is a prime number
    # results in # being copied and then pasted one at a time
    # therefore op_count = n
    if prime_factor == 1:
        # copy operation
        clipboard = file_text
        op_count += 1

        # paste operation for prime numbers
        file_text = n * clipboard
        op_count += n - 1
        return op_count

    while prime_factor > 1:
        prime_factor = 1

        for factor in range(2, int(chosen_factor / 2)):
            if chosen_factor % factor == 0:
                prime_factor = factor
                p_factors.append(prime_factor)

                chosen_factor = chosen_factor / factor
                break

        if prime_factor == 1:
            break

    # copy operation
    clipboard = file_text
    op_count += 1
    # paste operation for prime numbers
    paste_num = int(chosen_factor)
    file_text = clipboard * paste_num
    op_count += paste_num - 1

    index: int = -1
    while file_text != "H" * n:
        # copy operation
        clipboard = file_text
        op_count += 1

        # paste operation
        paste_num = p_factors[index] - 1
        file_text += clipboard * paste_num
        op_count += paste_num

        index -= 1

    return op_count
