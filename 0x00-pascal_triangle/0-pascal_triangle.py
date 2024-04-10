#!/usr/bin/python3
'''Module to return pascal triangle'''


def pascal_triangle(n):
    '''
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    '''
    storage = []
    if n == 0:
        return storage
    for initial in range(n):
        storage.append([])
        storage[initial].append(1)
        if (initial > 0):
            for just in range(1, initial):
                storage[initial].append(storage[initial - 1][just - 1] + storage[initial - 1][just])
            storage[initial].append(1)
    return storage
