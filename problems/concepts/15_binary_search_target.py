"""Binary Search practice: Find a target index.

Problem
Given a sorted list of distinct integers, return target's index or -1.

Feynman idea
Look at the middle. Because the list is sorted, one entire half is guaranteed
to be useless. Throw that half away and repeat.

Time: O(log n)
Space: O(1)
"""


def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    assert binary_search(nums, 7) == 3
    assert binary_search(nums, 8) == -1
    print("ok")
