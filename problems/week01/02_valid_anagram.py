# Problem: Valid Anagram
# Difficulty: Easy
# Pattern: String / Frequency Map
#
# Given two strings s and t, return True if t is an anagram of s.
# An anagram contains exactly the same characters with the same frequencies,
# but the characters may appear in a different order.
#
# Examples:
# s = "anagram", t = "nagaram" -> True
# s = "rat",     t = "car"     -> False
# s = "aacc",    t = "ccac"    -> False
#
# Rules for this practice:
# - Do not use sorted().
# - Do not use collections.Counter.
# - Build the frequency map directly with a dictionary.
#
# Initial attempt:
#
# def is_anagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#
#     counts = {}
#
#     for sChar in s:
#         counts[sChar] = counts.get(sChar, 0) + 1
#
#     for tChar in t:
#         counts[tChar] = counts.get(tChar, 0) - 1
#
#     return !all(counts)
#
# Correction:
# - Python uses "not" instead of "!" for logical negation.
# - Iterating over a dict directly produces its keys, not its values.
# - The required check is whether every frequency value equals zero.

# 한국어 문제 설명:
# 문자열 s와 t가 같은 문자들을 같은 개수만큼 포함하고 있는지 판별한다.
# 문자 순서는 달라도 되지만, 각 문자의 빈도는 완전히 같아야 한다.
#
# 내가 처음 작성한 알고리즘의 빈도 계산 방식은 맞았다.
# 다만 마지막 반환식에서 두 가지 Python 문법을 혼동했다.
#
# - Python의 논리 부정은 !가 아니라 not을 사용한다.
# - Dictionary를 직접 순회하면 값이 아니라 키가 나온다.
# - 여기서는 counts.values()의 모든 값이 0인지 확인해야 한다.
# - 따라서 all(count == 0 for count in counts.values())를 사용한다.


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = {}

    for s_char in s:
        counts[s_char] = counts.get(s_char, 0) + 1

    for t_char in t:
        counts[t_char] = counts.get(t_char, 0) - 1

    return all(count == 0 for count in counts.values())


# Verification
assert is_anagram("anagram", "nagaram") is True
assert is_anagram("rat", "car") is False
assert is_anagram("aacc", "ccac") is False
assert is_anagram("", "") is True

# Complexity / 복잡도:
# Time / 시간: O(N)
# Space / 공간: O(K), where K is the number of distinct characters.
# K는 서로 다른 문자의 개수다.
