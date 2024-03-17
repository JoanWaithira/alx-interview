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
    if len(boxes) == 0:
        return False

    visited = [False] * len(boxes)
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
