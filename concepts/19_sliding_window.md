# Sliding Window

## 한 문장

Sliding Window는 **배열 위에 일정한 구간을 잡고, 그 구간을 옆으로 밀면서 필요한 값을 갱신하는 기법**이다.

## 예시: 길이 3 구간의 최대합

```text
[1, 2, 3, 4, 5]
```

첫 창문:

```text
[1, 2, 3] = 6
```

다음 창문:

```text
[2, 3, 4]
```

처음부터 다시 더할 필요가 없다.

```text
기존 합 6 - 빠지는 1 + 들어오는 4 = 9
```

다음:

```text
9 - 2 + 5 = 12
```

## 코드

```python
def max_window_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for right in range(k, len(arr)):
        left = right - k

        window_sum -= arr[left]
        window_sum += arr[right]

        max_sum = max(max_sum, window_sum)

    return max_sum
```

## 핵심 원리

창문 전체를 다시 계산하지 않는다.

```text
새 구간 값 = 기존 구간 값 - 나가는 값 + 들어오는 값
```

그래서 고정 길이 구간을 매우 효율적으로 처리한다.

## 가변 길이 Window

조건에 따라 오른쪽 포인터로 범위를 넓히고, 조건이 만족되면 왼쪽 포인터를 움직여 줄일 수도 있다.

```text
[L ........ R]
```

예:

- 합이 S 이상인 가장 짧은 연속 구간
- 중복 없는 가장 긴 부분 문자열

## Two Pointers와 차이

Two Pointers는 두 위치를 움직이는 기법 전체를 말한다.

Sliding Window는 **두 포인터 사이의 연속 구간 자체를 유지/관리하는 것**이 핵심이다.

## 언제 떠올릴까?

- 연속된 K개
- 연속 부분 배열/문자열
- 구간이 한 칸씩 이동한다.
- 이전 구간 계산을 재활용할 수 있다.

## 기억법

> Sliding Window = 창문을 옆으로 밀면서, 나간 것 하나 빼고 들어온 것 하나 더한다.
