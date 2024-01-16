#!/usr/bin/python3
"""0-minoperations"""


def minOperations(n):
    """calculates the fewest number of operations needed to
    result in exactly n H characters in the file."""

    factors = []

    if n <= 1:
        return 0

    for i in range(2, int(n ** .5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 1:
        factors.append(n)

    return sum(factors)
