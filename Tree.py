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

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        while n > 0:
            b = a + b
            a = b
            n -= 1
        return a

import numba

@numba.njit
def fibonacci2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        while n > 0:
            b = a + b
            a = b
            n -= 1
        return a
    
