# Queue / Deque

## 한 문장

Queue는 **은행 대기줄처럼 먼저 들어온 것이 먼저 나오는 구조**다.

```text
A -> B -> C
A가 가장 먼저 들어왔으므로 A부터 처리
```

이 방식을 FIFO(First In, First Out)라고 한다.

## Python에서는 deque

```python
from collections import deque

queue = deque()
queue.append("A")
queue.append("B")
queue.append("C")

print(queue.popleft())  # A
```

## 왜 list.pop(0)을 잘 안 쓰나?

```python
arr = [1, 2, 3, 4]
arr.pop(0)
```

0번 원소를 지우면 나머지를 전부 한 칸씩 왼쪽으로 옮겨야 한다.

```text
[1, 2, 3, 4]
    ↓
[2, 3, 4]
```

그래서 `list.pop(0)`은 O(N)이다.

반면:

```python
queue.popleft()
```

는 O(1)이다.

## Deque란?

Deque = Double Ended Queue.

앞과 뒤 양쪽에서 넣고 뺄 수 있다.

```python
from collections import deque

dq = deque([10, 20])
dq.append(30)       # 오른쪽 추가
dq.appendleft(5)    # 왼쪽 추가

dq.pop()            # 오른쪽 제거
dq.popleft()        # 왼쪽 제거
```

## BFS와의 관계

BFS는 가까운 노드부터 처리해야 하므로 먼저 발견한 노드를 먼저 꺼낸다.

```python
from collections import deque

queue = deque([start])

while queue:
    node = queue.popleft()
```

그래서 BFS의 핵심 자료구조가 Queue다.

## 언제 떠올릴까?

- 먼저 들어온 순서대로 처리
- BFS
- 작업 대기열
- 고정 길이 구간 관리
- 양쪽 끝을 빠르게 조작

## 기억법

> Queue = 은행 줄. Deque = 앞문과 뒷문이 모두 있는 줄.
