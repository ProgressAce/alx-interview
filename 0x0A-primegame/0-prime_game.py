#!/usr/bin/python3
"""This module solves the prime game challenge."""


def generatePrimes(n):
    """Builds up all the prime numbers from 2 up to the given number.

    Uses the Sieve of Eratosthenes to efficiently find the prime numbers up
    to n. This algorithm is efficient for numbers before 10 million.
    Returns:
        a list of all the prime numbers found up to `n`."""

    prime_nums = [True for x in range(n + 1)]

    i = 2  # i indicates the index _and_ value of a prime number in prime_nums
    while i * i <= n:
        if prime_nums[i]:
            for multiple in range(i * i, n + 1, i):
                prime_nums[multiple] = False

        i += 1

    primes = []
    for i in range(n + 1):
        if prime_nums[i]:
            primes.append(i)

    return primes


def isWinner(x, nums):
    """
    Determines the winner for `x` games, dependant on the primes and multiples
    in `nums`.
    """
    maria_score = 0
    ben_score = 0
    game = 1

    for n in nums:
        # entire game should end when the game count exceeds x (total rounds)
        if game > x:
            break
        primes = generatePrimes(n)

        if len(primes) % 2 == 1 and len(primes) != 0:
            maria_score += 1
        else:
            ben_score += 1

    if maria_score > ben_score:
        return 'Maria'
    if ben_score > maria_score:
        return 'Ben'

    return None  # should indicate a draw
