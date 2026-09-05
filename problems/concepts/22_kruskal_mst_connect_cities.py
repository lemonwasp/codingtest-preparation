"""Kruskal / MST practice: Connect all cities at minimum total cost.

Problem
Given n cities and undirected weighted edges (a, b, cost), return the minimum
cost needed to connect every city. Return -1 if full connection is impossible.

Feynman idea
Sort roads from cheapest to most expensive. Take a road only when it connects
two groups that are currently separate. Union-Find answers that question
quickly and prevents cycles.

Time: O(E log E)
Space: O(V + E)
"""


def minimum_connection_cost(n: int, edges: list[tuple[int, int, int]]) -> int:
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a: int, b: int) -> bool:
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            return False

        if rank[root_a] < rank[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1
        return True

    total_cost = 0
    used_edges = 0

    for a, b, cost in sorted(edges, key=lambda edge: edge[2]):
        if union(a, b):
            total_cost += cost
            used_edges += 1

            if used_edges == n - 1:
                return total_cost

    return -1


if __name__ == "__main__":
    edges = [
        (1, 2, 1),
        (2, 3, 2),
        (1, 3, 3),
        (3, 4, 4),
    ]
    assert minimum_connection_cost(4, edges) == 7
    print("ok")
