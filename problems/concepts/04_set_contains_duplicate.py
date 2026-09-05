"""Set / hash practice: Contains duplicate.

Problem
Return True if any integer appears at least twice.

Feynman idea
A set is a membership desk. Before adding a number, ask: "Have I already
seen this member?" Hashing makes that membership test O(1) on average.

Time: O(n) average
Space: O(n)
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    print("ok")
