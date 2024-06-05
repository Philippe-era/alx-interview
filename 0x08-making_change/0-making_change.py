#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to give to user"""


def makeChange(coins, total):
    """This function gives change back to the user
    """
    if total <= 0:
        return 0

    else:
        coin_check = sorted(coins)
        coin_check.reverse()
        counter_add = 0
        for initial in coin_check:
            while(total >= initial):
                counter_add += 1
                total -= initial
        if total == 0:
            return counter_add
        return -1
