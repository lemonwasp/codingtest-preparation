# Dijkstra

## 한 문장

Dijkstra는 **출발점에서 현재 가장 가까운 노드부터 확정해 가며 최단거리를 구하는 알고리즘**이다.

길마다 비용이 다르지만 음수 간선은 없을 때 사용한다.

## 예시

```text
A -> B = 10
A -> C = 2
C -> B = 3
```

A에서 B로 바로 가면 10이지만 C를 거치면:

```text
2 + 3 = 5
```

더 짧다.

## 핵심 아이디어

1. 출발점 거리는 0, 나머지는 무한대로 둔다.
2. 현재 알고 있는 거리 중 가장 작은 노드를 꺼낸다.
3. 그 노드를 거쳐 이웃으로 가는 길이 더 짧은지 확인한다.
4. 더 짧으면 거리를 갱신하고 Priority Queue에 넣는다.
5. 반복한다.

## 코드

```python
import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for next_node, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heapq.heappush(pq, (new_distance, next_node))

    return distances
```

## Relaxation

```python
new_distance = current_distance + weight
```

현재 노드를 거쳐 다음 노드로 가는 새 경로를 계산한다.

```python
if new_distance < distances[next_node]:
```

기존 기록보다 짧다면 갈아치운다.

이 과정을 Relaxation이라고 한다.

## 왜 Heap을 쓰나?

매 순간 **현재 후보 중 가장 거리가 짧은 노드**를 꺼내야 하기 때문이다.

```python
heapq.heappop(pq)
```

Heap을 사용하면 최소 후보를 O(log N)에 꺼낼 수 있다.

## 오래된 정보 버리기

```python
if current_distance > distances[current_node]:
    continue
```

Heap에 예전에 넣은 더 긴 경로가 남아 있을 수 있다. 현재 최단거리보다 큰 값이라면 이미 더 좋은 길을 찾았으므로 버린다.

## 제한

음수 간선이 있으면 Dijkstra를 사용하면 안 된다.

## 시간복잡도

Heap + 인접 리스트 기준 보통:

```text
O(E log V)
```

## 기억법

> Dijkstra = 지금 가장 가까운 도시부터 처리하고, 더 짧은 길을 발견하면 거리표를 고친다.
