#!/usr/bin/python3
"""
Main file for testing
"""

import sys

minOperations = __import__("0-minoperations").minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

# case with 1 and less
print("\nCases of # as 1 or less")
print("Min # of operations to reach {} char: {}".format(1, minOperations(1)))
print("Min # of operations to reach {} char: {}".format(0, minOperations(0)))
print("Min # of operations to reach {} char: {}".format(-29, minOperations(-29)))
print("Min # of operations to reach {} char: {}".format(-24111, minOperations(-24111)))

# case with prime numbers
print("\nCases of # as prime numbers")
print("Min # of operations to reach {} char: {}".format(2, minOperations(2)))
print("Min # of operations to reach {} char: {}".format(3, minOperations(3)))
print("Min # of operations to reach {} char: {}".format(5, minOperations(5)))
print("Min # of operations to reach {} char: {}".format(7, minOperations(7)))

# case with non-prime odd numbers
print("\nCases of # as non-prime odd numbers")
print("Min # of operations to reach {} char: {}".format(9, minOperations(9)))
print("Min # of operations to reach {} char: {}".format(21, minOperations(21)))
print("Min # of operations to reach {} char: {}".format(81, minOperations(81)))
print(
    "Min # of operations to reach {} char: {}".format(19170307, minOperations(19170307))
)

# case with non-prime even numbers
print("\nCases of # as non-prime even numbers")
print("Min # of operations to reach {} char: {}".format(4, minOperations(4)))
print("Min # of operations to reach {} char: {}".format(12, minOperations(12)))
print("Min # of operations to reach {} char: {}".format(24, minOperations(24)))
print("Min # of operations to reach {} char: {}".format(842, minOperations(842)))

# case with number greater than max int or less than min int
max_int = 2147483640
# print(
#    "Min # of operations to reach {} char: {}".format(max_int, minOperations(max_int))
# )
