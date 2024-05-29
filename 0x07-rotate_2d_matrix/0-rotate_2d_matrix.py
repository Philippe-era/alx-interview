#!/usr/bin/python3
"""Spins the 2D matrix"""


def rotate_2d_matrix(matrix):
    """
       Spins 2D matrix 90 degrees clockwise
       Matrix is edited in-place
       args:
          matrix
    """
    left_side, right_side = 0, len(matrix) - 1

    while left_side < right_side:
        for initial in range(right_side - left_side):
            top_side, bottom_side = left_side, right_side
            
            topLeft = matrix[top_side][left_side + initial]
        
            matrix[top_side][left_side + initial] = matrix[bottom_side - initial][left_side]
            
            matrix[bottom_side - initial][left_side] = matrix[bottom_side][right_side - initial]
            
            matrix[bottom_side][right_side - initial] = matrix[top_side + initial][right_side]
            
            matrix[top_side + initial][right_side] = topLeft
            right_side -= 1
            left_side += 1

