"""Heap Sort algorithm implemented using our own heap.

Time complexity:
- Build heap: O(n)
- Each extract: O(log n)
- Total: O(n log n)

This file intentionally does NOT use Python's `heapq`.
"""

from __future__ import annotations

from typing import Iterable, List, TypeVar

from .heap import BinaryHeap, _default_cmp

T = TypeVar("T")


def heap_sort(values: Iterable[T], reverse: bool = False) -> List[T]:
    """Return a new list sorted using heap sort.

    If reverse=False (default): ascending order.
    If reverse=True: descending order.
    """
    if reverse:
        def cmp(a: T, b: T) -> int:
            return -_default_cmp(a, b)
    else:
        cmp = _default_cmp

    h = BinaryHeap.from_iterable(values, cmp=cmp)
    out: List[T] = []
    while len(h) > 0:
        out.append(h.pop())
    return out
