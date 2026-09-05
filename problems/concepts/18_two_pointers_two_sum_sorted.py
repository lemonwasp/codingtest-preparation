"""Two Pointers practice: Two sum in a sorted array.

Problem
Given a sorted list and target, return indices of two values whose sum equals
target, or None if no pair exists.

Feynman idea
Put one hand on the smallest value and one on the largest. If the sum is too
small, move the left hand right to increase it. If too large, move the right
hand left to decrease it.

Time: O(n)
Space: O(1)
"""


def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return left, right
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return None


if __name__ == "__main__":
    assert two_sum_sorted([1, 2, 4, 6, 10], 8) == (1, 3)
    assert two_sum_sorted([1, 2, 3], 10) is None
    print("ok")
