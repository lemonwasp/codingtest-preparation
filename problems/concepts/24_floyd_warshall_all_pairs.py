"""Floyd-Warshall practice: All-pairs shortest paths.

Problem
Given n nodes and directed weighted edges, return the shortest distance
between every ordered pair of nodes.

Feynman idea
For every possible middle node k, ask one question for every pair (i, j):
"Is i -> k -> j cheaper than the best i -> j route I already know?"
Repeatedly allowing more middle nodes builds the final all-pairs answer.

Time: O(V^3)
Space: O(V^2)
"""


def floyd_warshall(
    n: int,
    edges: list[tuple[int, int, int]],
) -> list[list[float]]:
    inf = float('inf')
    distance = [[inf] * (n + 1) for _ in range(n + 1)]

    for node in range(1, n + 1):
        distance[node][node] = 0

    for a, b, cost in edges:
        distance[a][b] = min(distance[a][b], cost)

    for middle in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                via_middle = distance[start][middle] + distance[middle][end]
                if via_middle < distance[start][end]:
                    distance[start][end] = via_middle

    return distance


if __name__ == "__main__":
    edges = [
        (1, 2, 10),
        (1, 3, 3),
        (3, 2, 2),
        (2, 4, 1),
        (3, 4, 8),
    ]
    distance = floyd_warshall(4, edges)
    assert distance[1][2] == 5
    assert distance[1][4] == 6
    assert distance[3][4] == 3
    print("ok")
