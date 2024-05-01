#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
