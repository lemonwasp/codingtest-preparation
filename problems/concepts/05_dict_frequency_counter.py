"""Dict / HashMap practice: Most frequent value.

Problem
Return the value that appears most often. If several values tie, returning
any one of them is acceptable.

Feynman idea
A dictionary is a labeled drawer: key = number, value = how many times it has
been seen. Update the drawer every time the number appears.

Time: O(n) average
Space: O(n)
"""


def most_frequent(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")

    counts: dict[int, int] = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    best_num = nums[0]
    best_count = counts[best_num]

    for num, count in counts.items():
        if count > best_count:
            best_num = num
            best_count = count

    return best_num


if __name__ == "__main__":
    assert most_frequent([1, 3, 3, 2, 3, 2]) == 3
    print("ok")
