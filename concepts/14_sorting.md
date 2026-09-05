# Sorting

## 한 문장

Sorting은 **데이터를 원하는 기준에 따라 줄 세우는 것**이다.

```text
5 2 8 1 3
↓
1 2 3 5 8
```

## Python 기본 정렬

```python
arr = [5, 2, 8, 1, 3]
arr.sort()
print(arr)
```

`sort()`는 원본을 바꾼다.

```python
arr = [5, 2, 8, 1, 3]
result = sorted(arr)
```

`sorted()`는 새 리스트를 만든다.

## 내림차순

```python
arr.sort(reverse=True)
```

## key가 중요한 이유

학생을 점수 기준으로 정렬한다고 하자.

```python
students = [
    ("Tom", 80),
    ("Alice", 95),
    ("Bob", 70),
]

students.sort(key=lambda x: x[1])
```

`lambda x: x[1]`은 각 학생에서 두 번째 값인 점수를 꺼내 정렬 기준으로 사용한다는 뜻이다.

## 여러 기준

점수는 높은 순, 점수가 같으면 이름순:

```python
students.sort(key=lambda x: (-x[1], x[0]))
```

Python은 튜플의 첫 번째 기준부터 비교한다.

## 왜 직접 버블 정렬을 잘 안 쓰나?

버블 정렬은 O(N²)이다.

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

Python의 `sort()`는 일반적으로 O(N log N)이므로 실전에서는 내장 정렬을 우선 사용한다.

## 언제 떠올릴까?

- 크기순/점수순/시간순으로 나열
- 이후 이진 탐색을 해야 한다.
- 그리디를 적용하기 전에 특정 기준으로 정리해야 한다.
- 같은 기준끼리 묶어 처리해야 한다.

## 기억법

> Sorting = 먼저 줄을 제대로 세워 놓으면 이후 문제 해결이 쉬워진다.
