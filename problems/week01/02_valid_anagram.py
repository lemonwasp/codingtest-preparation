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

# Complexity:
# Time: O(N)
# Space: O(K), where K is the number of distinct characters.
