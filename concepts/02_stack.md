# Stack

## 한 문장

Stack은 **접시 더미처럼 마지막에 넣은 것을 가장 먼저 꺼내는 구조**다.

```text
    C  <- 마지막에 넣음, 가장 먼저 꺼냄
    B
    A
```

이 방식을 LIFO(Last In, First Out)라고 한다.

## Python 구현

```python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack.pop())  # C
print(stack.pop())  # B
```

Python에서는 보통 별도의 Stack 클래스 없이 `list`를 사용한다.

## 왜 필요한가?

가장 최근의 상태를 먼저 처리해야 하는 문제에 적합하다.

예를 들어 괄호 `([])`를 검사한다고 하자.

```text
(  -> 저장
[  -> 저장
]  -> 가장 최근 [ 와 짝
)  -> 가장 최근 ( 와 짝
```

최근에 열린 괄호가 먼저 닫혀야 하므로 Stack이 맞다.

## DFS와의 관계

재귀 DFS도 내부적으로 함수 호출을 Stack에 쌓는다.

```text
dfs(1)
  dfs(2)
    dfs(4)
```

`dfs(4)`가 끝나면 `dfs(2)`로 돌아가고, 그다음 `dfs(1)`로 돌아온다.

## 시간복잡도

```python
stack.append(x)  # 평균 O(1)
stack.pop()      # O(1)
stack[-1]        # 맨 위 확인 O(1)
```

## 언제 떠올릴까?

- 괄호 검사
- 되돌리기(undo)
- DFS
- 백트래킹
- 최근 상태부터 처리

## 기억법

> Stack = 접시 더미. 마지막에 올린 접시부터 꺼낸다.
