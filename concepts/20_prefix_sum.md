# Prefix Sum

## 한 문장

Prefix Sum(누적합)은 **앞에서부터의 합을 미리 저장해 두고, 나중에 구간합을 뺄셈 한 번으로 구하는 기법**이다.

## 예시

```python
arr = [2, 4, 1, 5, 3]
```

누적합을 만들면:

```text
prefix = [0, 2, 6, 7, 12, 15]
```

의미는:

```text
prefix[0] = 0
prefix[1] = 2
prefix[2] = 2 + 4
prefix[3] = 2 + 4 + 1
...
```

## 왜 앞에 0을 넣나?

`prefix[i]`를 "arr의 0번부터 i-1번까지의 합"으로 통일할 수 있기 때문이다.

그러면 left부터 right까지의 합은 항상 같은 공식으로 계산된다.

```python
prefix[right + 1] - prefix[left]
```

## 코드

```python
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]

    return prefix


def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

## 왜 뺄셈으로 구간합이 나오나?

```text
arr = [2, 4, 1, 5, 3]
```

인덱스 1~3의 합을 구하면:

```text
4 + 1 + 5 = 10
```

누적합으로는:

```text
prefix[4] = 2 + 4 + 1 + 5 = 12
prefix[1] = 2
12 - 2 = 10
```

앞부분을 통째로 빼면 원하는 구간만 남는다.

## 시간복잡도

누적합 생성:

```text
O(N)
```

구간합 질의 하나:

```text
O(1)
```

구간합 질문이 매우 많을 때 큰 효과가 있다.

## Sliding Window와 차이

- Prefix Sum: 임의의 여러 구간 합을 빠르게 질의
- Sliding Window: 연속 구간을 옆으로 이동하면서 상태를 관리

## 기억법

> Prefix Sum = 앞에서부터 영수증 합계를 미리 적어 두고, 원하는 구간은 앞부분을 빼서 구한다.
