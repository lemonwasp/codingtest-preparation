# Binary Search

## 한 문장

Binary Search는 **정렬된 데이터에서 가운데를 보고 필요 없는 절반을 계속 버리는 탐색 방법**이다.

```text
[1, 3, 5, 7, 9]
```

7을 찾는다고 하자.

가운데 5를 본다. 7은 5보다 크므로 왼쪽 절반은 볼 필요가 없다.

```text
[7, 9]
```

이 과정을 반복한다.

## 기본 코드

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

## 왜 정렬되어 있어야 하나?

`arr[mid] < target`이라는 사실만으로 왼쪽 전체를 버리려면 왼쪽 값들이 모두 더 작다는 보장이 필요하다.

정렬되어 있지 않으면 절반을 버릴 근거가 없다.

## 왜 `mid + 1`, `mid - 1`인가?

`mid`는 이미 확인했으므로 다음 탐색 범위에서 제외한다.

```python
left = mid + 1
right = mid - 1
```

## 시간복잡도

매번 절반씩 줄어든다.

```text
1000 -> 500 -> 250 -> 125 -> ...
```

그래서 O(log N).

## bisect

Python에는 이진 탐색 도구가 있다.

```python
from bisect import bisect_left, bisect_right

arr = [1, 2, 2, 2, 5]

print(bisect_left(arr, 2))   # 1
print(bisect_right(arr, 2))  # 4
```

특정 값의 개수:

```python
count = bisect_right(arr, 2) - bisect_left(arr, 2)
```

## Parametric Search

정답 자체를 이진 탐색하는 응용이다.

> 어떤 높이까지 가능한가?
> 가능한 최대/최소 값은 무엇인가?

조건을 만족하면 한쪽 범위를 버리는 구조를 만든다.

## 기억법

> Binary Search = 정렬되어 있으면 가운데를 보고 절반을 버린다.
