# BFS (Breadth-First Search)

## 한 문장

BFS는 **시작점에서 가까운 곳부터 한 층씩 탐색하는 방법**이다.

물에 돌을 던졌을 때 물결이 퍼지는 모습을 생각하면 된다.

```text
        1
      /   \
     2     3
    /       \
   4         5

BFS: 1 -> 2 -> 3 -> 4 -> 5
```

## 왜 Queue를 쓰나?

먼저 발견한 노드를 먼저 처리해야 하기 때문이다.

```python
from collections import deque

queue = deque([start])
```

은행 대기줄처럼 FIFO 구조가 필요하다.

## 기본 코드

```python
from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()
        print(node)

        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
```

## 한 줄씩

```python
queue = deque([start])
```
시작점을 대기줄에 넣는다.

```python
visited = {start}
```
이미 방문했다고 표시한다. 이 기록이 없으면 그래프에서 같은 곳을 계속 돌 수 있다.

```python
node = queue.popleft()
```
가장 먼저 들어온 노드를 꺼낸다.

```python
for next_node in graph[node]:
```
현재 노드에서 바로 갈 수 있는 곳을 본다.

```python
if next_node not in visited:
```
아직 방문하지 않았다면 방문 표시 후 Queue 뒤에 넣는다.

## 왜 최단거리에 강한가?

모든 간선 비용이 같다면 거리 1인 곳을 전부 본 뒤 거리 2인 곳을 보고, 그다음 거리 3을 본다.

따라서 어떤 목적지를 처음 발견한 순간 그 경로가 최단거리다.

## 시간복잡도

인접 리스트 기준:

```text
O(V + E)
```

각 노드와 간선을 거의 한 번씩 확인한다.

## 언제 떠올릴까?

- 최소 이동 횟수
- 미로 최단거리
- 가장 가까운 대상
- 모든 이동 비용이 동일한 그래프

## 기억법

> BFS = 가까운 놈부터. Queue를 쓴다.
