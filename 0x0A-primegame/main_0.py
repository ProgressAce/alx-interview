#!/usr/bin/python3
""" One case of the isWinner function
"""

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))