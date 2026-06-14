from dataclasses import dataclass
from typing import Union

@dataclass
class Empty:
    """Base Case: An empty leaf boundary."""
    pass

@dataclass
class Node:
    """Recursive Case: A node containing data and two sub-trees."""
    value: int
    left: 'Tree'
    right: 'Tree'

# Define the Tree ADT as a Union of the two possible states
Tree = Union[Empty, Node]

def tree_sum(tree: Tree) -> int:
    """Recursively processes the Tree ADT using structural pattern matching."""
    match tree:
        case Empty():
            return 0  # Base Case
        case Node(value, left, right):
            return value + tree_sum(left) + tree_sum(right)  # Recursive Case

# Construct a recursive Tree:
#       5
#      / \
#     3   Empty
