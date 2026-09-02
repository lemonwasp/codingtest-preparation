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

# 한국어 문제 설명:
# 정수 배열 nums와 정수 target이 주어질 때, 합이 target이 되는
# 두 원소의 인덱스를 반환한다.
#
# 핵심 관찰:
# 현재 숫자 number를 확인할 때 필요한 짝은 target - number이다.
# 이전에 본 숫자와 인덱스를 Dictionary에 저장하면 필요한 숫자의
# 존재 여부를 평균 O(1)에 확인할 수 있다.
#
# 현재 숫자를 Dictionary에 넣기 전에 needed를 먼저 검사해야
# 같은 배열 원소를 두 번 사용하는 오류를 피할 수 있다.


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

# Complexity / 복잡도:
# Time / 시간: O(N)
# Space / 공간: O(N)
