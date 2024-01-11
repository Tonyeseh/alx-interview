#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1 and
    each box may contain keys to the other boxes.
    The first box boxes[0] is unlocked

    determines if all the boxes can be opened.

    boxes: is a list of lists

    Return True if all boxes can be opened, else return False
    """
    keys = [0, ]

    for box in range(len(boxes)):
        if box not in keys:
            return False
        keys += boxes[box]
    return True
