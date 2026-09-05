"""Heap / priority queue practice: Kth largest element.

Problem
Return the kth largest number in an unsorted list.

Feynman idea
Keep a min-heap containing only the k largest values seen so far. The smallest
value inside that elite group is exactly the kth largest overall.

Time: O(n log k)
Space: O(k)
"""

import heapq


def kth_largest(nums: list[int], k: int) -> int:
    if k < 1 or k > len(nums):
        raise ValueError("k out of range")

    heap: list[int] = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


if __name__ == "__main__":
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    print("ok")
