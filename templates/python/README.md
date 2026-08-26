# Python Coding-Test Templates

The goal of this folder is **memory reinforcement**, not copy-paste dependency.

Add a template only after you have implemented the pattern successfully several times.

## Core Syntax to Memorize in Weeks 1-2

```python
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right

# input
n = int(input())
a = list(map(int, input().split()))

# hash
freq = Counter(a)
seen = set(a)
graph = defaultdict(list)

# sorting
b = sorted(a)
a.sort(reverse=True)

# queue
q = deque([0])
x = q.popleft()
q.append(x)

# heap
heap = []
heappush(heap, 3)
x = heappop(heap)

# binary-search helpers
left = bisect_left(a, x)
right = bisect_right(a, x)
```

## Templates to Earn

Do not fill these by copying an editorial. Add each one only when the underlying pattern is understood.

- binary search
- BFS
- DFS
- two pointers
- sliding window
- prefix sum
- heap
- union-find
- topological sort
- Dijkstra
- 1D DP
- 2D DP

For every template, write:

1. when to use it;
2. invariant / key idea;
3. complexity;
4. common bug;
5. minimal implementation.
