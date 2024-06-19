#!/usr/bin/python3
"""
Module: Prime numbers to be checked
"""


def primeNumbers(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime_nums = []
    excluded_nums = [True] * (n + 1)
    for prime_check in range(2, n + 1):
        if (excluded_nums[prime_check]):
            prime_nums.append(prime_check)
            for initial in range(prime, n + 1, prime_check):
                excluded_nums[initial] = False
    return prime_nums


def isWinner(x, nums):
    """
    This tells us who won
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for initial in range(x):
        prime_nums = primeNumbers(nums[initial])
        if len(prime_nums) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
