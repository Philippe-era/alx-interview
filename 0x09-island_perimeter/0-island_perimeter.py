#!/usr/bin/python3
"""
Island Perimeter:
    returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """island perimenter function"""
    peri = 0
    for initial in range(len(grid)):
        for join in range(len(grid[initial])):
            if grid[initial][join] == 1:
                peri += 4
                if initial > 0 and grid[initial-1][join] == 1:
                    peri -= 2
                if join > 0 and grid[initial][join-1] == 1:
                    peri -= 2
    return peri
