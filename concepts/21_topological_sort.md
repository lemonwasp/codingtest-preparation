# Topological Sort

## 한 문장

Topological Sort(위상정렬)는 **선행 조건이 있는 작업들을 가능한 순서대로 나열하는 알고리즘**이다.

예:

```text
프로그래밍 기초 -> 자료구조 -> 알고리즘 -> 코딩테스트
```

앞의 과정을 끝내야 뒤의 과정을 할 수 있다.

## 핵심 개념: 진입차수(indegree)

진입차수는 **현재 작업보다 먼저 끝나야 하는 작업의 개수**다.

```text
A -> C
B -> C
C -> D
```

진입차수:

```text
A = 0
B = 0
C = 2
D = 1
```

A와 B는 바로 시작 가능하다.

## 알고리즘

1. indegree가 0인 노드를 Queue에 넣는다.
2. Queue에서 하나 꺼내 결과에 추가한다.
3. 그 노드가 끝났으므로 연결된 다음 노드들의 indegree를 1 줄인다.
4. indegree가 0이 된 노드는 Queue에 넣는다.
5. 반복한다.

## 코드

```python
from collections import deque


def topological_sort(n, graph, indegree):
    queue = deque()

    for node in range(1, n + 1):
        if indegree[node] == 0:
            queue.append(node)

    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for next_node in graph[current]:
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                queue.append(next_node)

    return result
```

## 왜 `indegree -= 1`인가?

```text
A -> C
B -> C
```

C는 A와 B 두 작업을 기다린다.

A가 끝나면:

```text
2 -> 1
```

B도 끝나면:

```text
1 -> 0
```

이제 C를 시작할 수 있다.

## DAG가 필요한 이유

위상정렬은 Directed Acyclic Graph에서 사용한다.

사이클이 있다면:

```text
A -> B -> C -> A
```

A는 C를 기다리고, C는 B를 기다리고, B는 A를 기다리므로 아무도 시작할 수 없다.

## 사이클 판별

결과에 들어간 노드 수가 전체 노드 수보다 작다면 사이클이 존재한다.

```python
if len(result) != n:
    print("cycle")
```

## 언제 떠올릴까?

- 선수과목
- 빌드 순서
- 작업 의존성
- 선행 작업
- 어떤 일을 먼저 해야 하는가?

## 기억법

> Topological Sort = 먼저 해야 할 일이 하나도 남지 않은 작업부터 처리한다.
