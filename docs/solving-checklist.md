# Problem-Solving Checklist

Use this checklist before, during, and after every problem.

## 1. Before Coding

- What are N and the other input limits?
- What time complexity is realistically allowed?
- Is brute force actually acceptable?
- What is the output asking for: existence, count, minimum/maximum, ordering, path, number of ways?
- Which known pattern does the problem resemble?
- What edge cases can break the obvious solution?

## 2. Choose the Approach

Write one sentence before implementation:

> I will use ______ because ______, giving O(______) time and O(______) space.

If you cannot fill this sentence, do not start coding yet.

## 3. While Coding

- keep variable meanings explicit
- avoid unnecessary abstraction during a timed test
- check empty / single-element cases
- check duplicate values
- check off-by-one boundaries
- check integer range if the language requires it
- stop and reassess if implementation becomes much more complicated than expected

## 4. Before Submit

Run at least these mental tests:

1. smallest valid input
2. all values equal
3. strictly increasing / decreasing input if relevant
4. duplicate-heavy input
5. answer at the first or last index
6. no-solution case if permitted

Then verify:

- input parsed correctly
- output format exact
- loop boundaries correct
- visited/state initialized correctly
- sorting direction correct
- complexity still fits maximum input

## 5. After Submit

### If Accepted

Record:
- key observation
- pattern
- time complexity
- one alternative approach
- one thing that could have caused a wrong answer

### If Wrong Answer

Classify the cause:
- misunderstood requirement
- wrong algorithm
- missing edge case
- off-by-one
- state/visited bug
- sorting/comparison bug
- input/output mistake
- implementation slip

### If Time Limit Exceeded

Record:
- actual complexity
- required complexity
- which constraint should have warned you

### If You Needed a Hint

Do not mark the problem as learned. Add it to the re-solve queue for D+1 / D+7 / D+21.
