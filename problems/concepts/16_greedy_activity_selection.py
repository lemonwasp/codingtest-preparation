"""Greedy practice: Maximum number of non-overlapping meetings.

Problem
Each meeting is (start, end). Return the maximum number of meetings one room
can hold without overlap.

Feynman idea
Always choose the meeting that finishes earliest. It leaves the most room for
everything that comes later. This local choice is safe for interval scheduling.

Time: O(n log n) for sorting
Space: O(n) depending on sorting/result representation
"""


def max_meetings(meetings: list[tuple[int, int]]) -> int:
    meetings = sorted(meetings, key=lambda meeting: (meeting[1], meeting[0]))

    count = 0
    end_time = float('-inf')

    for start, end in meetings:
        if start >= end_time:
            count += 1
            end_time = end

    return count


if __name__ == "__main__":
    meetings = [(1, 4), (3, 5), (4, 7), (5, 6), (6, 8)]
    assert max_meetings(meetings) == 3
    print("ok")
