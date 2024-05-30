#!/usr/bin/python3
"""Spins a 2D matrix"""

def rotate_2d_matrix(matrix):
    """
       Spins 2D matrix 90 degrees clockwise
       Matrix is edited in-place
       args:
          matrix
    """

    left_pos, right_pos = 0, len(matrix) - 1

    while left_pos < right_pos:
        for initial in range(right_pos - left_pos):
            top, bottom = left_pos, right_pos

            topLeft = matrix[top][left_pos + initial]

            matrix[top][left_pos + initial] = matrix[bottom - initial][left_pos]

            matrix[bottom - initial][left_pos] = matrix[bottom][right_pos - initial]

            matrix[bottom][right_pos - initial] = matrix[top + initial][right_pos]

            matrix[top + initial][right_pos] = topLeft
        right_pos -= 1
        left_pos += 1
