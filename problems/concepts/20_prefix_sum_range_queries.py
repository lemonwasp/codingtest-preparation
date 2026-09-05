"""Prefix Sum practice: Answer range-sum queries.

Problem
Build a prefix-sum array so each inclusive query [left, right] can be answered
in O(1).

Feynman idea
prefix[i] stores the sum of everything before index i. The sum inside a range
is the large prefix minus the part before the range.

Build: O(n)
Each query: O(1)
Space: O(n)
"""


def build_prefix(nums: list[int]) -> list[int]:
    prefix = [0] * (len(nums) + 1)

    for i, num in enumerate(nums):
        prefix[i + 1] = prefix[i] + num

    return prefix


def range_sum(prefix: list[int], left: int, right: int) -> int:
    return prefix[right + 1] - prefix[left]


if __name__ == "__main__":
    nums = [2, 4, 1, 5, 3]
    prefix = build_prefix(nums)
    assert range_sum(prefix, 1, 3) == 10
    assert range_sum(prefix, 0, 4) == 15
    print(prefix)
