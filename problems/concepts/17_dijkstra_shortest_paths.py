"""Dijkstra practice: Shortest paths from one source.

Problem
Given a directed graph with non-negative edge weights, return the shortest
distance from start to every node.

Feynman idea
Keep a priority queue of discovered routes. Always expand the currently
cheapest route first. If a newly found route to a neighbor is cheaper than the
old one, replace the old distance and push the new candidate.

Time: O((V + E) log V)
Space: O(V + E)
"""

import heapq


def dijkstra(
    n: int,
    graph: list[list[tuple[int, int]]],
    start: int,
) -> list[float]:
    inf = float('inf')
    distance = [inf] * (n + 1)
    distance[start] = 0

    heap: list[tuple[int, int]] = [(0, start)]

    while heap:
        current_distance, node = heapq.heappop(heap)

        if current_distance > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = current_distance + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distance


if __name__ == "__main__":
    graph = [
        [],
        [(2, 10), (3, 2)],
        [(4, 1)],
        [(2, 3), (4, 7)],
        [],
    ]
    distance = dijkstra(4, graph, 1)
    assert distance[1:] == [0, 5, 2, 6]
    print(distance[1:])
