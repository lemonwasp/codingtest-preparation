"""Dynamic Programming practice: Climbing stairs.

Problem
You may climb 1 or 2 steps at a time. Return the number of distinct ways to
reach step n.

Feynman idea
To reach step i, the previous position must have been i-1 or i-2. Therefore
ways[i] = ways[i-1] + ways[i-2]. Store earlier answers instead of recomputing
them.

Time: O(n)
Space: O(n)
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(5) == 8
    print("ok")
