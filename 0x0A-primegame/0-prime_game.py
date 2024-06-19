#!/usr/bin/python3
"""
Module: Prime numbers being checked
"""


def primeNumbers(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime_nums = []
    excluded = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (excluded[prime]):
            prime_nums.append(prime)
            for initial in range(prime, n + 1, prime):
                excluded[initial] = False
    return prime_nums


def isWinner(x, nums):
    """
    Tells who will win the game
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
