# Coding Test Preparation

A focused repository for building coding-test skill through reusable problem-solving patterns, timed practice, and structured review.

## Goal

**Pass coding tests consistently within 8 weeks.**

This repository is not a collection of random solved problems. Every solution should strengthen one of three things:

1. **Recognition** — identify the right algorithm/data structure quickly.
2. **Implementation** — write a correct solution without searching for syntax.
3. **Review** — turn mistakes into reusable rules and templates.

## 8-Week Target

| Phase | Weeks | Focus | Exit condition |
|---|---:|---|---|
| Foundation | 1-2 | Complexity, arrays, strings, hash, stack/queue, sorting | Easy problems mostly solved in 15-20 min |
| Core Patterns | 3-4 | Binary search, two pointers, prefix sum, greedy, BFS/DFS | Medium-pattern recognition becomes reliable |
| Algorithms | 5-6 | Graphs, heaps, DP, union-find, shortest path | Can combine 2 patterns under time pressure |
| Simulation | 7-8 | Timed sets, company-style mock tests, weak-point repair | 3 mock tests in a row at target pass level |

Detailed plan: [`docs/8-week-roadmap.md`](docs/8-week-roadmap.md)

## Study Rules

- Primary language: **Python 3** for speed and concise implementation.
- Solve first without AI or editorial help.
- If stuck for **25 minutes**, record the blocker before reading a hint.
- Re-solve failed or heavily assisted problems after **1 day, 7 days, and 21 days**.
- A problem is not complete when Accepted; it is complete when the core pattern can be explained from memory.
- Prefer **30 well-reviewed problems** over 100 copied solutions.

## Repository Structure

```text
.
├── docs/
│   ├── 8-week-roadmap.md
│   └── solving-checklist.md
├── templates/
│   └── python/
│       └── README.md
├── problems/
│   └── week01/
│       └── README.md
└── reviews/
    └── mistake-log.md
```

## Per-Problem Record

Each problem entry should contain:

```text
Problem:
Platform / URL:
Difficulty:
Pattern:
Time to first solution:
Result: solved / hint / failed

1. What was the key observation?
2. Why does the chosen algorithm fit the constraints?
3. Time / space complexity?
4. What mistake or hesitation occurred?
5. What rule should be remembered next time?
```

## Weekly Success Metrics

Track these instead of raw problem count:

- first-attempt solve rate
- median solve time
- number of hint-dependent problems
- number of repeated mistakes
- re-solve success rate
- timed mock-test pass rate

## Definition of Ready

At the end of 8 weeks, the target is to be able to:

- classify common problems within roughly 3-5 minutes;
- implement core patterns from memory;
- finish easy problems reliably and medium problems selectively under time limits;
- detect impossible approaches from input constraints before coding;
- explain complexity and edge cases immediately after solving;
- maintain performance across several timed mock tests, not just isolated practice problems.
