#!/usr/bin/python3
"""0-rotate_2d_matrix"""

def rotate_2d_matrix(matrix):
    """Rotate a 2d matrix 90 degrees clockwise"""
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(len(matrix)):
        for j in range(len(matrix) // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][len(matrix) - 1 - j]
            matrix[i][len(matrix) - 1 - j] = temp
