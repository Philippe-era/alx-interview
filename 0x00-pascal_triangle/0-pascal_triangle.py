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
    lists = []
    if n == 0:
        return lists
    for initial in range(n):
        lists.append([])
        lists[initial].append(1)
        if (initial > 0):
            for j in range(1, initial):
                lists[initial].append(lists[initial - 1][j - 1] + lists[initial - 1][j])
            lists[initial].append(1)
    return lists
