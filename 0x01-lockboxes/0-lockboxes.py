#!/usr/bin/python3
"""Defines a function for checking if all given boxes can unlock."""


def canUnlockAll(boxes):
    """Checks if the list of boxes can all be unlcoked.

    Each box is numbered sequentially from 0 to n - 1 and each box
    may contain keys to the other boxes. A key with the same number
    as a box opens that box.

    All keys are assumed to be positive integers.
    There can be keys that do not have boxes.
    The first box <boxes[0]> is assumed to be unlocked.

    Args:
        boxes(list of lists): the container holding all the boxes inside it.
    Returns:
        True, if all boxes can be opened, else returns False.
    """

    total_boxes = len(boxes)
    open_count = 1
    unused_keys = set()

    # test arg
    if not isinstance(boxes, list):
        raise TypeError("boxes should be a list of lists of positive integers")

    for value in boxes[0]:
        unused_keys.add(value)

    new_keys = [1]  # initial value used so while loop can start
    used_keys = {
        0,
    }
    while len(used_keys) < total_boxes and len(new_keys) != 0:
        new_keys = set()

        #        print("used keys:", used_keys)
        #        print("unused keys:", unused_keys)

        for key in unused_keys:
            if key < total_boxes:  # only a key with an existing box is used
                open_count += 1
                used_keys.add(key)

                for value in boxes[key]:  # store keys found in a box
                    new_keys.add(value)

        # remove the keys which were already used
        unused_keys = new_keys
        unused_keys.difference_update(used_keys)

    if open_count == total_boxes:
        return True

    return False
