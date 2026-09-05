"""Topological Sort practice: Course order.

Problem
There are n courses labeled 0..n-1. Each prerequisite pair (a, b) means b
must be completed before a. Return one valid order, or [] if a cycle exists.

Feynman idea
A course with indegree 0 has no unfinished prerequisite, so it can be taken
now. Remove it from the graph, decrease the indegree of dependent courses,
and repeat.

Time: O(V + E)
Space: O(V + E)
"""

from collections import deque


def course_order(n: int, prerequisites: list[tuple[int, int]]) -> list[int]:
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1

    queue = deque(course for course in range(n) if indegree[course] == 0)
    order: list[int] = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    return order if len(order) == n else []


if __name__ == "__main__":
    order = course_order(4, [(1, 0), (2, 0), (3, 1), (3, 2)])
    assert order[0] == 0
    assert order[-1] == 3
    assert course_order(2, [(0, 1), (1, 0)]) == []
    print(order)
