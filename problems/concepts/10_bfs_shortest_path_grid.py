"""BFS practice: Shortest path in an unweighted grid.

Problem
0 means open and 1 means blocked. Starting at (0, 0), return the minimum
number of moves needed to reach the bottom-right cell, or -1 if impossible.

Feynman idea
BFS spreads like ripples in water. It visits every cell 1 move away, then 2
moves away, then 3. Therefore the first time we reach the goal is the shortest
path when every move has the same cost.

Time: O(rows * cols)
Space: O(rows * cols)
"""

from collections import deque


def shortest_path(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1

    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        row, col, distance = queue.popleft()

        if (row, col) == (rows - 1, cols - 1):
            return distance

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            if grid[nr][nc] == 1 or (nr, nc) in visited:
                continue

            visited.add((nr, nc))
            queue.append((nr, nc, distance + 1))

    return -1


if __name__ == "__main__":
    grid = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 0, 0],
    ]
    assert shortest_path(grid) == 4
    print("ok")
