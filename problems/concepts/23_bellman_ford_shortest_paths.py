"""Bellman-Ford practice: Shortest paths with negative edges.

Problem
Given n nodes and directed weighted edges, return shortest distances from
start. If a reachable negative cycle exists, return None.

Feynman idea
Relax every edge repeatedly. A shortest simple path can use at most V-1 edges,
so after V-1 full rounds all normal shortest distances must be settled. If one
more round still improves a distance, a reachable negative cycle exists.

Time: O(VE)
Space: O(V)
"""


def bellman_ford(
    n: int,
    edges: list[tuple[int, int, int]],
    start: int,
) -> list[float] | None:
    inf = float('inf')
    distance = [inf] * (n + 1)
    distance[start] = 0

    for _ in range(n - 1):
        updated = False

        for current, next_node, cost in edges:
            if distance[current] == inf:
                continue

            new_distance = distance[current] + cost

            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                updated = True

        if not updated:
            break

    for current, next_node, cost in edges:
        if distance[current] == inf:
            continue

        if distance[current] + cost < distance[next_node]:
            return None

    return distance


if __name__ == "__main__":
    edges = [
        (1, 2, 4),
        (1, 3, 5),
        (2, 3, -2),
        (3, 4, 3),
    ]
    distance = bellman_ford(4, edges, 1)
    assert distance is not None
    assert distance[1:] == [0, 4, 2, 5]

    negative_cycle = [(1, 2, 1), (2, 3, -2), (3, 2, -2)]
    assert bellman_ford(3, negative_cycle, 1) is None
    print("ok")
