"""Sliding Window practice: Maximum sum of a fixed-size subarray.

Problem
Return the maximum sum among all contiguous subarrays of length k.

Feynman idea
A window of k values slides one step at a time. Do not sum the whole window
again. Subtract the value that leaves and add the value that enters.

Time: O(n)
Space: O(1)
"""


def max_window_sum(nums: list[int], k: int) -> int:
    if k < 1 or k > len(nums):
        raise ValueError("invalid k")

    window_sum = sum(nums[:k])
    best = window_sum

    for right in range(k, len(nums)):
        left = right - k
        window_sum -= nums[left]
        window_sum += nums[right]
        best = max(best, window_sum)

    return best


if __name__ == "__main__":
    assert max_window_sum([1, 2, 3, 4, 5], 3) == 12
    assert max_window_sum([4, -1, 2, 1], 2) == 3
    print("ok")
