"""Backtracking practice: Generate permutations.

Problem
Return all permutations of distinct integers.

Feynman idea
Choose one number, explore everything that can follow it, then undo that
choice and try the next number. append = choose, recursive call = explore,
pop = undo.

Time: O(n * n!)
Space: O(n) recursion excluding output
"""


def permutations(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            result.append(path.copy())
            return

        for i, num in enumerate(nums):
            if used[i]:
                continue

            used[i] = True
            path.append(num)

            backtrack()

            path.pop()
            used[i] = False

    backtrack()
    return result


if __name__ == "__main__":
    result = permutations([1, 2, 3])
    assert len(result) == 6
    assert [1, 2, 3] in result
    assert [3, 2, 1] in result
    print(result)
