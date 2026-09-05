# Bellman-Ford

## 한 문장

Bellman-Ford는 **음수 간선이 있어도 사용할 수 있는 단일 출발점 최단거리 알고리즘**이다.

또한 **음수 사이클**도 감지할 수 있다.

## 왜 Dijkstra 대신 필요한가?

Dijkstra는 음수 간선이 있으면 현재 가장 가까운 노드를 확정한다는 논리가 깨질 수 있다.

Bellman-Ford는 특정 노드를 일찍 확정하지 않고 **모든 간선을 반복해서 확인하며 더 짧은 길을 계속 갱신**한다.

## 핵심 아이디어

노드가 V개일 때 사이클 없는 최단 경로는 최대 V-1개의 간선을 사용한다.

그래서 모든 간선을 V-1번 반복해서 Relaxation한다.

## 코드

```python
def bellman_ford(n, edges, start):
    INF = float("inf")
    distance = [INF] * (n + 1)
    distance[start] = 0

    for _ in range(n - 1):
        updated = False

        for current, next_node, cost in edges:
            if distance[current] == INF:
                continue

            new_distance = distance[current] + cost

            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                updated = True

        if not updated:
            break

    return distance
```

## Relaxation

```python
new_distance = distance[current] + cost
```

현재 노드를 거쳐 다음 노드로 가는 새 비용을 계산한다.

```python
if new_distance < distance[next_node]:
    distance[next_node] = new_distance
```

기존 거리보다 짧으면 갱신한다.

## 음수 사이클

예:

```text
B -> C = -5
C -> B = 1
```

한 바퀴 비용은 -4다.

계속 돌면:

```text
-4, -8, -12, ...
```

거리값이 끝없이 작아진다. 따라서 최단거리 자체가 존재하지 않는다.

## 음수 사이클 감지 코드

```python
def bellman_ford(n, edges, start):
    INF = float("inf")
    distance = [INF] * (n + 1)
    distance[start] = 0

    for i in range(n):
        for current, next_node, cost in edges:
            if distance[current] == INF:
                continue

            new_distance = distance[current] + cost

            if new_distance < distance[next_node]:
                distance[next_node] = new_distance

                if i == n - 1:
                    return None  # 시작점에서 도달 가능한 음수 사이클

    return distance
```

V-1번이면 정상 최단거리는 모두 계산되어야 한다. V번째 반복에서도 갱신된다면 음수 사이클 때문에 계속 줄어드는 것이다.

## 시간복잡도

```text
O(VE)
```

Dijkstra보다 느리지만 음수 간선을 처리할 수 있다.

## 언제 떠올릴까?

- 한 출발점 최단거리
- 음수 가중치가 있음
- 음수 사이클 판별

## 기억법

> Bellman-Ford = 모든 도로를 계속 훑으면서 더 싼 길이 있으면 고친다. 끝까지 계속 싸진다면 음수 사이클이다.
