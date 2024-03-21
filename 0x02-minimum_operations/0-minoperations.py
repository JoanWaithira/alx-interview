#!/usr/bin/python3
""" Minimum operations """


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in a text file.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed.
             If n is impossible to achieve, return 0.
    """
    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
