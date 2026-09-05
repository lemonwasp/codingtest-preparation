"""Sorting practice: Sort student records by multiple keys.

Problem
Each record is (name, score). Sort by score descending, then name ascending.

Feynman idea
Sorting is lining people up by rules. Python compares tuple keys from left to
right, so (-score, name) means score first (reversed by the minus sign), then
name for ties.

Time: O(n log n)
Space: O(n) implementation-dependent
"""


def sort_students(students: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(students, key=lambda student: (-student[1], student[0]))


if __name__ == "__main__":
    students = [("Charlie", 90), ("Alice", 90), ("Bob", 80)]
    assert sort_students(students) == [
        ("Alice", 90),
        ("Charlie", 90),
        ("Bob", 80),
    ]
    print(sort_students(students))
