"""Heap / priority queue practice: Kth largest element.

Problem
Return the kth largest number in an unsorted list.

Feynman idea
Imagine keeping only the current "top k" scores in a small box.
Whenever a new number arrives, put it in the box. If the box now contains more
than k values, remove the smallest one. After every number has been processed,
the smallest value remaining in the box is the kth largest overall.

Why a min-heap?
We must repeatedly remove the smallest value from the current top-k group.
A min-heap gives us that value at heap[0] and removes it in O(log k).

Time: O(n log k)
Space: O(k)
"""

import heapq


def kth_largest(nums: list[int], k: int) -> int:
    """Return the kth largest value using a size-k min-heap."""
    if not nums:
        raise ValueError("nums must not be empty")
    if k < 1 or k > len(nums):
        raise ValueError("k out of range")

    heap: list[int] = []

    for num in nums:
        heapq.heappush(heap, num)

        # Only the k largest values seen so far are allowed to remain.
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


def _run_tests() -> None:
    # Typical case.
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

    # Duplicates still count as separate elements.
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    # k == 1 means the maximum value.
    assert kth_largest([-5, -2, -9], 1) == -2

    # k == len(nums) means the minimum value.
    assert kth_largest([7, 4, 9], 3) == 4

    # Invalid input should fail explicitly instead of returning a wrong result.
    for nums, k in [([], 1), ([1, 2], 0), ([1, 2], 3)]:
        try:
            kth_largest(nums, k)
        except ValueError:
            pass
        else:
            raise AssertionError(f"expected ValueError for nums={nums}, k={k}")


if __name__ == "__main__":
    _run_tests()
    print("all heap practice tests passed")
