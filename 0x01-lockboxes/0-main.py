#!/usr/bin/python3
"""Main file for using 0-lockboxes.py"""

canUnlockAll = __import__("0-lockboxes").canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

# all keys are assumed to be positive integers
print(canUnlockAll([[], [2], [3]]))  # empty first box - false
print(canUnlockAll(""))  # string arg - TypeError
print(canUnlockAll(5))  # integer arg - TypeError
print(canUnlockAll([]))  # 1-D array arg - TypeError
print(canUnlockAll({5: 12, 1: 45}))  # dict arg - TypeError
