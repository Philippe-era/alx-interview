#!/usr/bin/python3
'''Module needed to perform this task '''

def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    tri = [[1]]
    for initial in range(1, n):
        previous = tri[-1]
        line = [1]
        for just in range(1, initial):
            line.append(previous[just-1] + previous[just])
            line.append(1)
            tri.append(line)
            return tri
