"""List / Array practice: Reverse an array in place.

Problem
Given a list of integers, reverse it without creating another result list.

Feynman idea
An array is like numbered lockers. Swap the locker at the left end with the
locker at the right end, then move both hands inward.

Time: O(n)
Extra space: O(1)
"""


def reverse_in_place(nums: list[int]) -> None:
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    reverse_in_place(nums)
    assert nums == [5, 4, 3, 2, 1]
    print(nums)
