"""Heap data structure (self-implemented).

This implementation uses an array-backed binary heap.
- MinHeap: smallest key at top
- MaxHeap: largest key at top

For the course project Task 2, we avoid using Python's `heapq`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, Iterable, List, Optional, TypeVar

T = TypeVar("T")


def _default_cmp(a: T, b: T) -> int:
    # returns negative if a<b, 0 if equal, positive if a>b
    return (a > b) - (a < b)


@dataclass
class BinaryHeap(Generic[T]):
    """A binary heap with a customizable comparator.

    If cmp(a,b) < 0, then a has higher priority than b.
    """

    cmp: Callable[[T, T], int] = _default_cmp
    _data: List[T] = None  # type: ignore

    def __post_init__(self) -> None:
        if self._data is None:
            self._data = []

    @classmethod
    def from_iterable(cls, items: Iterable[T], cmp: Callable[[T, T], int] = _default_cmp) -> "BinaryHeap[T]":
        h = cls(cmp=cmp)
        h._data = list(items)
        h._heapify()
        return h

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return not self._data

    def peek(self) -> T:
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def push(self, value: T) -> None:
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty heap")
        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return top

    def as_list(self):
        return list(self._data)
    # --- internal helpers ---

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _higher_priority(self, a: T, b: T) -> bool:
        return self.cmp(a, b) < 0

    def _sift_up(self, i: int) -> None:
        while i > 0:
            p = self._parent(i)
            if self._higher_priority(self._data[i], self._data[p]):
                self._data[i], self._data[p] = self._data[p], self._data[i]
                i = p
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self._data)
        while True:
            l = self._left(i)
            r = self._right(i)
            best = i
            if l < n and self._higher_priority(self._data[l], self._data[best]):
                best = l
            if r < n and self._higher_priority(self._data[r], self._data[best]):
                best = r
            if best != i:
                self._data[i], self._data[best] = self._data[best], self._data[i]
                i = best
            else:
                break

    def _heapify(self) -> None:
        # bottom-up heapify
        n = len(self._data)
        for i in range((n // 2) - 1, -1, -1):
            self._sift_down(i)


def min_heap(items: Optional[Iterable[T]] = None) -> BinaryHeap[T]:
    h = BinaryHeap[T](cmp=_default_cmp)
    if items is not None:
        h = BinaryHeap.from_iterable(items, cmp=_default_cmp)
    return h


def max_heap(items: Optional[Iterable[T]] = None) -> BinaryHeap[T]:
    def cmp(a: T, b: T) -> int:
        return -_default_cmp(a, b)  # reverse

    h = BinaryHeap[T](cmp=cmp)
    if items is not None:
        h = BinaryHeap.from_iterable(items, cmp=cmp)
    return h

