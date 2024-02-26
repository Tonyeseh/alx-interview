#!/usr/bin/python3
"""0-making_change"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    """
    count = 0
    if total < 1:
        return count

    if not coins:
        return -1

    min_val = min(coins)
    max_val = coins.pop(coins.index(max(coins)))

    if total < min_val:
        return -1

    while total >= max_val:
        total = total - max_val
        count += 1

    new_count = makeChange(coins, total)
    if new_count == -1:
        return -1

    return count + new_count
