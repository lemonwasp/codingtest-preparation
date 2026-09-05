"""Union-Find practice: Count connected components.

Problem
There are n nodes. Given undirected edges, return how many disconnected
groups remain.

Feynman idea
Each node starts as its own team captain. union(a, b) merges two teams, while
find(x) follows parent links to discover the captain. Path compression makes
future searches much faster.

Time: O((V + E) * alpha(V)) amortized
Space: O(V)
"""


def count_components(n: int, edges: list[tuple[int, int]]) -> int:
    parent = list(range(n))
    rank = [0] * n

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

    components = n

    for a, b in edges:
        if union(a, b):
            components -= 1

    return components


if __name__ == "__main__":
    assert count_components(5, [(0, 1), (1, 2), (3, 4)]) == 2
    print("ok")
