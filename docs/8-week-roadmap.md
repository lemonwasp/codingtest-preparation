# 8-Week Coding Test Roadmap

## Operating Principle

The goal is not to maximize solved-problem count. The goal is to make common patterns automatic enough to survive a timed coding test.

Recommended weekly load: **8-10 hours**.

- Weekdays: 45-75 minutes x 5
- Weekend: one 2-3 hour timed/review block
- Every session: solve -> review -> record

## Week 1 — Baseline + Core Implementation

Focus:
- Big-O and constraint reading
- arrays / strings
- hash map / set
- sorting
- stack / queue
- basic simulation

Target:
- 12-15 problems
- 80% of easy problems within 20 minutes
- no syntax lookup for dictionary, set, sorting, deque

Checkpoint:
- 60-minute mini mock: 3 easy problems

## Week 2 — Search and Sequence Patterns

Focus:
- binary search
- two pointers
- sliding window
- prefix sum
- interval handling

Target:
- 12-15 problems
- identify O(N^2) traps from constraints before coding
- binary-search boundaries implemented from memory

Checkpoint:
- 75-minute mock: 2 easy + 1 medium

## Week 3 — Greedy + Traversal

Focus:
- greedy reasoning
- BFS / DFS
- grid traversal
- connected components
- recursion vs iterative traversal

Target:
- 12-14 problems
- write BFS/DFS templates from memory
- explain why a greedy choice is safe instead of relying on intuition

Checkpoint:
- one medium graph/grid problem under 35 minutes

## Week 4 — Heaps + Graph Foundations

Focus:
- heap / priority queue
- graph representation
- topological sort
- union-find
- shortest-path intuition

Target:
- 10-12 problems
- distinguish BFS, Dijkstra, and union-find use cases quickly

Checkpoint:
- 90-minute mixed mock

## Week 5 — Dynamic Programming I

Focus:
- 1D DP
- 2D DP
- state definition
- recurrence construction
- memoization vs tabulation

Target:
- 10-12 problems
- state the DP state and recurrence before implementation

Checkpoint:
- solve 2 unfamiliar DP problems without copying a recurrence

## Week 6 — Dynamic Programming II + Mixed Mediums

Focus:
- knapsack-style DP
- subsequences
- combinational states
- graph + DP / greedy + sorting combinations

Target:
- 8-10 medium problems
- reduce time spent deciding between candidate approaches

Checkpoint:
- 120-minute mock with 3-4 mixed problems

## Week 7 — Timed Test Mode

Focus:
- no new broad topic unless a major gap remains
- timed sets
- input parsing speed
- debugging discipline
- skip / return strategy

Target:
- 3 full mocks
- review every failure on the same day
- re-solve failed problems 24 hours later

Pass rule:
- target score reached in at least 2 of 3 mocks

## Week 8 — Weak-Point Repair + Company Simulation

Focus:
- only recurring mistakes and high-frequency patterns
- realistic time limits
- no external help during mocks

Target:
- 4 full mocks
- 3 consecutive mocks at pass level
- no recurring implementation mistake appears twice in the final week

## Pattern Priority

### Tier A — Must be automatic

- arrays / strings
- hash map / set
- sorting
- stack / queue
- binary search
- two pointers / sliding window
- prefix sum
- BFS / DFS
- heap
- greedy basics

### Tier B — Must be usable

- union-find
- topological sort
- Dijkstra
- 1D / 2D DP

### Tier C — Learn only after A/B are stable

- advanced string algorithms
- segment tree / Fenwick tree
- advanced graph theory
- advanced combinatorics

## Review Schedule

For every failed or hint-dependent problem:

- D+1: re-solve from scratch
- D+7: re-solve without notes
- D+21: final retention check

If the same mistake happens twice, add it to `reviews/mistake-log.md` as a named rule.

## Promotion Rule

A pattern is considered learned only when all are true:

1. You can recognize it from constraints and structure.
2. You can implement it without syntax search.
3. You can explain correctness at a high level.
4. You can state time and space complexity.
5. You can solve a variation of it later without looking at the old answer.
