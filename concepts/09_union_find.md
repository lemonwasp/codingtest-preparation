# Union-Find

## 한 문장

Union-Find는 **두 원소가 같은 그룹에 속해 있는지 빠르게 확인하고, 그룹끼리 합치는 자료구조**다.

처음에는 모두 따로 있다.

```text
{1} {2} {3} {4}
```

1과 2를 합치고, 2와 3을 합치면:

```text
{1,2,3} {4}
```

이제 1과 3이 같은 그룹인지 빠르게 확인할 수 있다.

## 핵심 아이디어

각 그룹에는 대표(root)가 하나 있다.

```python
parent = [i for i in range(n + 1)]
```

처음에는 각자 자기 자신이 대표다.

## find

```python
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
```

`find(x)`는 x가 속한 그룹의 대표를 찾는다.

`parent[x] = find(...)`는 경로 압축(Path Compression)이다. 한 번 대표를 찾고 나면 다음부터 대표에게 바로 연결해 탐색을 빠르게 만든다.

## union

```python
def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a == root_b:
        return False

    parent[root_b] = root_a
    return True
```

두 대표가 같다면 이미 같은 그룹이다.

다르면 한 그룹의 대표를 다른 그룹 대표에 연결한다.

## Kruskal과의 관계

Kruskal은 간선을 하나 고를 때마다 질문한다.

> 이 두 노드는 이미 연결되어 있는가?

이미 연결되어 있다면 새 간선을 추가할 경우 사이클이 생긴다.

그래서 Union-Find로 빠르게 확인한다.

## 언제 떠올릴까?

- 같은 그룹인가?
- 연결 여부를 반복해서 확인한다.
- 여러 집합을 합친다.
- Kruskal / MST
- 사이클 판별

## 기억법

> Union-Find = 사람마다 팀 대표를 두고, 대표가 같으면 같은 팀이라고 판단한다.
