# Dict / HashMap

## 한 문장

Dict는 **이름표(key)를 주면 연결된 값(value)을 바로 꺼내는 전화번호부**다.

```python
scores = {
    "Alice": 90,
    "Bob": 75,
}

print(scores["Alice"])  # 90
```

## 구조

```text
Alice -> 90
Bob   -> 75
```

List는 위치(index)로 값을 찾지만 Dict는 key로 값을 찾는다.

## 핵심 원리

Python의 dict는 Hash Table을 기반으로 한다.

```text
key
 ↓
hash 계산
 ↓
저장 위치
 ↓
value
```

그래서 key 조회, 추가, 수정은 평균 O(1)이다.

## 빈도수 세기

코딩테스트에서 가장 자주 쓰는 패턴 중 하나다.

```python
arr = [1, 1, 2, 3, 3, 3]
counts = {}

for num in arr:
    counts[num] = counts.get(num, 0) + 1

print(counts)
# {1: 2, 2: 1, 3: 3}
```

### `get(num, 0)`은 무슨 뜻인가?

```python
counts.get(num, 0)
```

- `num`이라는 key가 있으면 기존 값을 반환
- 없으면 기본값 0을 반환

따라서 처음 3을 보면:

```text
0 + 1 = 1
```

다음 3을 보면:

```text
1 + 1 = 2
```

## 순회

```python
for key, value in counts.items():
    print(key, value)
```

## 언제 떠올릴까?

- 각 값이 몇 번 나왔는가?
- 이름/ID에 대응하는 정보를 저장해야 하는가?
- 두 데이터 사이 매핑이 필요한가?
- 빠른 key 조회가 필요한가?

## 기억법

> Dict = 이름을 말하면 바로 정보를 찾아주는 전화번호부.
