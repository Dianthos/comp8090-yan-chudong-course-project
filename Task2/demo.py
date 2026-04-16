"""Quick demo for Task 2.

Run:
  python -m task2.demo
"""

from __future__ import annotations

from .heap import max_heap
from .heap_sort import heap_sort


def main() -> None:
    data = [5, 1, 9, 2, 7, 3, 8, 4, 6]
    print("Original:", data)

    h = max_heap(data)
    print("Heap internal array:", h.as_list())
    extracted = [h.pop() for _ in range(len(h))]
    print("Pop all (descending):", extracted)

    print("Heap sort (ascending):", heap_sort(data))
    print("Heap sort (descending):", heap_sort(data, reverse=True))


if __name__ == "__main__":
    main()
