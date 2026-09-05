# MST / Kruskal

## 한 문장

MST(Minimum Spanning Tree)는 **모든 노드를 연결하면서 전체 연결 비용을 최소로 만드는 트리**다.

Kruskal은 MST를 만드는 대표 알고리즘으로 **가장 싼 간선부터 고르되 사이클은 만들지 않는다.**

## 예시

```text
A-B = 1
B-C = 2
A-C = 3
C-D = 4
```

비용순으로 본다.

```text
A-B 1  -> 선택
B-C 2  -> 선택
A-C 3  -> 이미 연결되어 있으므로 선택하면 사이클, 버림
C-D 4  -> 선택
```

모든 노드가 연결되었다.

## 왜 간선이 N-1개인가?

노드 N개를 사이클 없이 모두 연결한 Tree는 항상 간선이 N-1개다.

## Union-Find가 필요한 이유

간선 `(a, b)`를 추가하기 전에 질문한다.

> a와 b가 이미 같은 그룹인가?

같은 그룹이면 이미 다른 경로로 연결되어 있으므로 새 간선을 넣으면 사이클이 생긴다.

## 코드

```python
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a == root_b:
        return False

    parent[root_b] = root_a
    return True


def kruskal(n, edges):
    parent = [i for i in range(n + 1)]
    edges.sort(key=lambda x: x[2])

    total_cost = 0
    selected = 0

    for a, b, cost in edges:
        if union(parent, a, b):
            total_cost += cost
            selected += 1

            if selected == n - 1:
                break

    return total_cost
```

## `edges.sort(key=lambda x: x[2])`

간선이 `(start, end, cost)` 형태라면 `x[2]`가 비용이다.

Kruskal은 가장 싼 간선부터 보므로 비용 기준 정렬이 첫 단계다.

## Dijkstra와 차이

- Dijkstra: 한 출발점에서 다른 노드들까지 최단거리
- Kruskal: 전체 네트워크를 만드는 최소 총비용

예:

- 서울에서 부산까지 가장 싼 경로 -> Dijkstra
- 전국 모든 도시를 최소 비용으로 통신망 연결 -> MST/Kruskal

## 시간복잡도

주요 비용은 간선 정렬이다.

```text
O(E log E)
```

## 기억법

> Kruskal = 가장 싼 다리부터 놓는다. 이미 연결된 두 땅 사이에는 새 다리를 놓지 않는다.
