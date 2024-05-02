"""Defines a function to solve the coin change problem."""


def makeChange(coins, total):
    """Makes change with the least amount of coins possible.

    It is assumed that:
    - we have an infinite number of each denomination
      of coin in the list.
    - the value of a coin will always be an integer greater than 0.

    Args:
        coins(list of int): all the available coins.
        total(int): the amount of change to make with the coins.

    Returns:
        the fewest number of coins needed to meet `total`
    """

    if total <= 0:
        return 0
    if not isinstance(coins, list) or len(coins) < 1:
        return -1

    dynamic_amounts = [float('inf') for i in range(total + 1)]

    dynamic_amounts[0] = 0
    for i, dyn_a in enumerate(dynamic_amounts):
        for coin in coins:
            # if true, then the coin can't be used for change i
            # since i, although an index, is looked at as change
            if (i - coin) < 0:
                continue

            prev_dynamic_amount = dynamic_amounts[i - coin]

            # define new minimum coin amount with the current iterated coin
            # taken into consideration
            new_min_amount = prev_dynamic_amount + 1
            old_min_amount = dynamic_amounts[i]

            # compare existing minimum coin amount to the newly found one.
            if new_min_amount < old_min_amount:
                dynamic_amounts[i] = new_min_amount

    return -1 if dynamic_amounts[-1] == float('inf') else \
        dynamic_amounts[-1]
