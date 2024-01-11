#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    if n <= 0:
        return []

    if n == 1:
        return [[1]]
    if n == 2:
        return [[1]] + [[1, 1]]

    triangle = [[1]] + [[1, 1]]

    for i in range(n - 2):
        prev_tri = triangle[-1]
        new_tri = [1, 1]
        for j in range(1, len(prev_tri)):
            new_tri.insert(1, prev_tri[j - 1] + prev_tri[j])

        triangle.append(new_tri)

    return triangle
