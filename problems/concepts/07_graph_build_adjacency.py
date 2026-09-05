"""Graph practice: Build an adjacency list and count degrees.

Problem
Given n undirected nodes and edges, build an adjacency list and return each
node's degree.

Feynman idea
A graph is a city map. For every road a-b, write b in a's neighbor list and a
in b's neighbor list.

Time: O(V + E)
Space: O(V + E)
"""


def build_graph(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    graph = [[] for _ in range(n + 1)]

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    return graph


def degrees(graph: list[list[int]]) -> list[int]:
    return [len(graph[node]) for node in range(1, len(graph))]


if __name__ == "__main__":
    graph = build_graph(4, [(1, 2), (1, 3), (3, 4)])
    assert degrees(graph) == [2, 1, 2, 1]
    print(graph)
