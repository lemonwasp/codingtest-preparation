# Backtracking

## 한 문장

Backtracking은 **선택해 보고, 조건에 맞지 않으면 그 선택을 취소하고 다른 선택을 시도하는 방법**이다.

```text
1 선택
  -> 2 선택 -> 완성
  -> 되돌아감
  -> 3 선택 -> 완성
```

## 기본 패턴

```python
def backtrack(path):
    if len(path) == 2:
        print(path)
        return

    for num in [1, 2, 3]:
        if num not in path:
            path.append(num)   # 선택
            backtrack(path)    # 더 깊이 탐색
            path.pop()         # 선택 취소
```

## 핵심은 세 단계

```python
path.append(num)
```
현재 선택을 한다.

```python
backtrack(path)
```
그 선택을 유지한 채 다음 단계로 간다.

```python
path.pop()
```
다른 경우를 시험하기 위해 방금 선택을 취소한다.

## DFS와 차이

Backtracking은 보통 DFS의 형태를 사용하지만 **필요 없는 경우를 일찍 포기(pruning)** 하는 것이 핵심이다.

예를 들어 합이 이미 목표보다 커졌다면 더 깊이 내려가지 않는다.

```python
if current_sum > target:
    return
```

## 언제 떠올릴까?

- 순열
- 조합
- 모든 가능한 경우
- N-Queen
- 스도쿠
- 조건을 만족하는 배치

## 기억법

> Backtracking = 일단 해 본다. 아니면 취소하고 다른 길로 간다.
