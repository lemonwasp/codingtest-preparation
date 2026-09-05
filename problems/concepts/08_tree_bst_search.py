"""Tree / BST practice: Search a binary search tree.

Problem
Return True if target exists in a BST.

Feynman idea
A BST is a sorted decision tree: values smaller than the current node are on
the left and larger values are on the right. At each node, one whole side can
be discarded.

Time: O(h), where h is tree height
Space: O(1) iterative
"""

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: 'Node | None' = None
    right: 'Node | None' = None


def bst_contains(root: Node | None, target: int) -> bool:
    current = root

    while current is not None:
        if current.value == target:
            return True
        if target < current.value:
            current = current.left
        else:
            current = current.right

    return False


if __name__ == "__main__":
    root = Node(8, Node(4, Node(2), Node(6)), Node(12, Node(10), Node(14)))
    assert bst_contains(root, 10) is True
    assert bst_contains(root, 7) is False
    print("ok")
