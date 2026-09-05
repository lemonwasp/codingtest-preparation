"""Stack practice: Valid parentheses.

Problem
Return True if (), [], and {} are correctly matched and nested.

Feynman idea
A stack is a pile of plates. The most recently opened bracket must be the
first one closed, so push opening brackets and pop when a closing bracket
arrives.

Time: O(n)
Space: O(n)
"""


def is_valid_parentheses(text: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack: list[str] = []

    for char in text:
        if char in '([{':
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack


if __name__ == "__main__":
    assert is_valid_parentheses("([]{})") is True
    assert is_valid_parentheses("([)]") is False
    print("ok")
