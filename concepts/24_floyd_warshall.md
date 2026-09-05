# Floyd-Warshall

## 한 문장

Floyd-Warshall은 **모든 노드에서 모든 노드까지의 최단거리를 한 번에 구하는 알고리즘**이다.

## 핵심 질문

항상 이것만 묻는다.

> i에서 j로 바로 가는 것보다 k를 거쳐 가는 것이 더 짧은가?

수식:

```python
dist[i][j] = min(
    dist[i][j],
    dist[i][k] + dist[k][j]
)
```

이 한 줄이 알고리즘의 핵심이다.

## 예시

```text
A -> B = 10
A -> C = 3
C -> B = 2
```

A에서 B로 직접 가면 10.

C를 거치면:

```text
3 + 2 = 5
```

따라서 A -> B의 최단거리를 5로 갱신한다.

## 거리표 만들기

모든 출발점과 도착점 조합이 필요하므로 2차원 배열을 사용한다.

```python
INF = float("inf")

dist = [
    [INF] * (n + 1)
    for _ in range(n + 1)
]
```

자기 자신까지 거리는 0이다.

```python
for i in range(1, n + 1):
    dist[i][i] = 0
```

직접 연결된 간선도 기록한다.

```python
for a, b, cost in edges:
    dist[a][b] = min(dist[a][b], cost)
```

같은 두 노드 사이에 여러 간선이 있을 수 있으므로 `min`을 사용한다.

## 전체 코드

```python
def floyd_warshall(n, edges):
    INF = float("inf")

    dist = [
        [INF] * (n + 1)
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):
        dist[i][i] = 0

    for a, b, cost in edges:
        dist[a][b] = min(dist[a][b], cost)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    return dist
```

## 왜 반복문이 k -> i -> j 순서인가?

`k`는 이번에 **중간 경유지로 허용할 노드**다.

```text
i -> j
```

와:

```text
i -> k -> j
```

를 모든 i, j 조합에 대해 비교한다.

그다음 다른 k를 경유지로 허용하며 가능한 경로를 점점 확장한다.

## 시간복잡도

반복문이 세 겹이므로:

```text
O(V^3)
```

노드 수가 매우 크면 비싸다.

## 최단거리 알고리즘 비교

```text
BFS            : 가중치가 동일한 한 출발점 최단거리
Dijkstra       : 음수 없는 한 출발점 최단거리
Bellman-Ford   : 음수 간선 가능한 한 출발점 최단거리
Floyd-Warshall : 모든 출발점-도착점 쌍의 최단거리
```

## 언제 떠올릴까?

- 모든 도시 사이 최단거리
- 모든 학생 사이 관계 거리
- N이 비교적 작고 모든 쌍의 답이 필요함

## 기억법

> Floyd-Warshall = 모든 i와 j에 대해 'k를 거쳐 가면 더 짧나?'를 전부 시험한다.
