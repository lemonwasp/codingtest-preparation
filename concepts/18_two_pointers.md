# Two Pointers

## 한 문장

Two Pointers는 **배열 위에 위치를 가리키는 변수 두 개를 두고, 조건에 따라 둘을 움직이며 답을 찾는 기법**이다.

## 양쪽 끝에서 시작하는 예

정렬된 배열에서 합이 9인 두 수를 찾자.

```text
[1, 2, 3, 4, 5, 7]
 ↑              ↑
left           right
```

현재 합은 1 + 7 = 8. 목표보다 작다.

합을 키우려면 더 큰 왼쪽 값을 써야 하므로 `left += 1` 한다.

```text
2 + 7 = 9
```

찾았다.

## 코드

```python
def find_pair(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None
```

## 왜 움직이는 방향을 결정할 수 있나?

배열이 정렬되어 있기 때문이다.

- 합이 작다 -> 더 큰 수가 필요 -> left를 오른쪽으로
- 합이 크다 -> 더 작은 수가 필요 -> right를 왼쪽으로

## 같은 방향 Two Pointers

둘 다 왼쪽에서 출발해 한 포인터가 범위를 넓히고 다른 포인터가 줄이는 형태도 있다.

```text
L .... R ->
```

이 형태는 Sliding Window와 자주 겹친다.

## 시간복잡도

각 포인터가 배열을 최대 한 번 정도 지나가므로 많은 문제를 O(N)에 해결할 수 있다.

## 언제 떠올릴까?

- 정렬된 배열에서 두 수의 합
- 연속 부분 배열
- 두 배열을 함께 훑기
- O(N²) 모든 쌍 탐색을 줄이고 싶을 때

## 기억법

> Two Pointers = 손가락 두 개를 배열 위에 올리고, 조건을 보며 움직인다.
