# Set / Hash

## 한 문장

Set은 **중복을 허용하지 않는 회원 명단**, Hash는 **이름을 계산해서 보관 위치를 바로 찾아가는 방법**이다.

```python
numbers = {1, 2, 3}
print(2 in numbers)  # True
```

## 왜 list보다 빠르게 찾을 수 있나?

List에서 `x in arr`를 하면 앞에서부터 확인해야 한다.

```text
[10, 20, 30, 40, ...]
10? 아니면 다음
20? 아니면 다음
...
```

최악의 경우 O(N).

Hash 구조는 key를 계산해서 저장 위치를 정한다.

```text
hash("Alice") -> 어떤 숫자 -> 특정 칸
```

다시 Alice를 찾을 때 같은 계산으로 그 칸에 바로 접근한다.

그래서 Set의 존재 확인은 평균 O(1)이다.

## 기본 사용법

```python
visited = set()

visited.add(3)
visited.add(5)
visited.add(3)  # 중복 추가되어도 하나만 존재

print(3 in visited)  # True
visited.remove(3)
```

## BFS / DFS에서 왜 자주 쓰나?

이미 방문했는지 빠르게 확인해야 한다.

```python
visited = {start}

if next_node not in visited:
    visited.add(next_node)
```

List를 쓰면 방문 여부를 확인할 때마다 O(N)이 될 수 있다.

## 중복 제거

```python
arr = [1, 1, 2, 2, 3]
unique = set(arr)
print(unique)  # {1, 2, 3}
```

## 주의

Hash의 O(1)은 평균 시간복잡도다. 충돌이 극단적으로 많으면 느려질 수 있지만 일반 코딩테스트에서는 평균 O(1)로 생각한다.

## 언제 떠올릴까?

- 값이 존재하는가?
- 중복을 제거해야 하는가?
- 이미 방문했는가?
- 빠른 membership test가 필요한가?

## 기억법

> Set = 중복 없는 명단. Hash = 이름을 보고 사물함 번호를 바로 계산한다.
