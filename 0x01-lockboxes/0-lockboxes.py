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
    box_state = [True] * len(boxes)

    for key in keys:
        try:
            found_keys = boxes[key]
            box_state[key] = False
        except Exception as e:
            pass

        for new_key in found_keys:
            if new_key not in keys:
                keys.append(new_key)

    if any(box_state):
        return False
    return True
