# Tree / Binary Search Tree

## 한 문장

Tree는 부모-자식 관계를 가진 계층 구조다. Binary Search Tree(BST)는 왼쪽에 작은 값, 오른쪽에 큰 값을 둔다.

```text
        8
       / \
      4   12
     / \  / \
    2  6 10 14
```

## 기본 용어

- Root: 맨 위 노드
- Parent: 위쪽 노드
- Child: 아래쪽 노드
- Leaf: 자식이 없는 노드
- Depth: 루트에서 내려온 단계 수

## BST 탐색 원리

10을 찾는다면 8보다 크므로 오른쪽으로 간다. 12보다 작으므로 왼쪽으로 간다. 이렇게 한쪽 범위를 버리면서 탐색한다.

## 간단한 순회 코드

```python
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)
```

BST를 중위 순회하면 값이 오름차순으로 나온다.

## Heap과의 차이

- BST: 탐색을 쉽게 하기 위한 왼쪽/오른쪽 크기 규칙
- Heap: 최솟값/최댓값을 빠르게 꺼내기 위한 부모/자식 우선순위 규칙

## 기억법

> Tree = 조직도. BST = 왼쪽에는 작은 값, 오른쪽에는 큰 값을 놓는 조직도.
