"""DFS practice: Number of islands.

Problem
In a grid of 1s (land) and 0s (water), count connected land groups using
4-directional movement.

Feynman idea
When we find one unvisited land cell, DFS walks through that entire island
before returning. After it finishes, every cell in that island is marked, so
the next unvisited 1 must belong to a new island.

Time: O(rows * cols)
Space: O(rows * cols) worst case recursion
"""


def count_islands(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row: int, col: int) -> None:
        if not (0 <= row < rows and 0 <= col < cols):
            return
        if grid[row][col] == 0:
            return

        grid[row][col] = 0

        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    islands = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                islands += 1
                dfs(row, col)

    return islands


if __name__ == "__main__":
    grid = [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
    ]
    assert count_islands(grid) == 2
    print("ok")
