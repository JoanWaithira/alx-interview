#!/usr/bin/python3
"""Alx interview Lockboxes"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing the boxes.
            Each inner list contains keys that correspond to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.

    Example:
        boxes = [[1], [2], [3], [4], []]
        canUnlockAll(boxes)  # Output: True
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
