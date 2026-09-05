# DFS (Depth-First Search)

## 한 문장

DFS는 **한 길을 가능한 끝까지 가 본 뒤, 더 갈 수 없으면 돌아와 다른 길을 탐색하는 방법**이다.

```text
        1
      /   \
     2     3
    /       \
   4         5

DFS 예: 1 -> 2 -> 4 -> 3 -> 5
```

## 기본 코드

```python
def dfs(graph, node, visited):
    visited.add(node)
    print(node)

    for next_node in graph[node]:
        if next_node not in visited:
            dfs(graph, next_node, visited)
```

사용:

```python
visited = set()
dfs(graph, 1, visited)
```

## 왜 재귀를 쓰나?

현재 노드에서 다음 노드로 들어가면 그 노드에서도 똑같은 일을 해야 한다.

```text
dfs(1)
  -> dfs(2)
      -> dfs(4)
```

4에서 더 갈 곳이 없으면 `dfs(4)`가 끝나고 `dfs(2)`로 돌아온다. 이것이 재귀 호출 스택이다.

## visited는 왜 필요한가?

그래프에는 사이클이 있을 수 있다.

```text
1 -> 2 -> 3 -> 1
```

방문 기록이 없으면 끝없이 돈다.

## 섬 문제의 전형적인 형태

```python
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if grid[x][y] == 0:
        return

    grid[x][y] = 0

    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)
```

`grid[x][y] = 0`은 방문한 땅을 다시 방문하지 않도록 표시하는 방법이다.

## 시간복잡도

인접 리스트 기준:

```text
O(V + E)
```

## 언제 떠올릴까?

- 연결된 영역을 전부 탐색
- 섬 개수
- 연결 요소
- 모든 경로 탐색
- 재귀/백트래킹의 기반

## 기억법

> DFS = 한 놈 끝까지. 더 못 가면 돌아온다.
