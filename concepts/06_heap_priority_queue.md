# Heap / Priority Queue

## 한 문장

Heap은 **가장 작은 값 또는 가장 큰 값을 빠르게 꺼내기 위한 자료구조**다.

Priority Queue는 먼저 온 순서가 아니라 **우선순위가 높은 것부터 처리하는 줄**이다.

## Python의 Min Heap

```python
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print(heapq.heappop(heap))  # 1
print(heapq.heappop(heap))  # 2
```

## Heap은 완전히 정렬된 배열인가?

아니다.

Heap은 전체를 정렬하는 대신 **부모가 자식보다 작다**는 규칙을 유지한다.

```text
       1
     /   \
    2     8
   / \
  5   7
```

그래서 맨 위(root)는 항상 가장 작다.

## 왜 빠른가?

트리는 한 층 내려갈 때 후보가 대략 두 배씩 늘어난다.

따라서 높이는 약 `log N`이다.

```text
heappush = O(log N)
heappop  = O(log N)
최솟값 확인 heap[0] = O(1)
```

## 우선순위와 데이터를 같이 저장

```python
pq = []

heapq.heappush(pq, (3, "A"))
heapq.heappush(pq, (1, "B"))
heapq.heappush(pq, (2, "C"))

print(heapq.heappop(pq))  # (1, 'B')
```

튜플은 앞의 값부터 비교하므로 첫 번째 값을 우선순위로 사용할 수 있다.

## Dijkstra와의 관계

다익스트라는 **현재 발견한 경로 중 거리가 가장 짧은 노드**를 계속 꺼내야 한다.

```python
heapq.heappush(pq, (distance, node))
current_distance, current_node = heapq.heappop(pq)
```

그래서 Heap/Priority Queue가 핵심 자료구조다.

## 언제 떠올릴까?

- 최솟값/최댓값을 반복해서 꺼낸다.
- 우선순위대로 작업한다.
- Dijkstra
- 상위 K개 / 하위 K개 관리

## 기억법

> Heap = 가장 급한 사람을 맨 앞에 유지하는 응급실 대기열.
