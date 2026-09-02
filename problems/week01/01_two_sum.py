# Problem: Two Sum
# Difficulty: Easy
# Pattern: Array / Hash Map
#
# Given a list of integers nums and an integer target, return the indices of
# two numbers whose sum equals target.
#
# Rules:
# - Exactly one valid answer exists.
# - The same element cannot be used twice.
# - Aim for O(N) time complexity.
#
# Examples:
# nums = [2, 7, 11, 15], target = 9  -> [0, 1]
# nums = [3, 2, 4], target = 6       -> [1, 2]
#
# Key observation:
# For each number, calculate the value still needed:
#     needed = target - number
# Store each previously visited number and its index in a dictionary.
# Looking up a key in a Python dict takes O(1) average time.


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for index, number in enumerate(nums):
        needed = target - number

        if needed in seen:
            return [seen[needed], index]

        # Check before inserting so the same element is not used twice.
        seen[number] = index

    return []


# Verification
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
assert two_sum([-3, 4, 3, 90], 0) == [0, 2]

# Complexity:
# Time: O(N)
# Space: O(N)
