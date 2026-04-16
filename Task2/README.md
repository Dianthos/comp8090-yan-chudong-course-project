
---

# `task2/README.md`

```md
# Task 2 - Binary Heap and Heap Sort

## Overview
This folder contains **Task 2** of the COMP8090SEF individual course project.

For this task, I studied and implemented:
- **Binary Heap** as the new data structure
- **Heap Sort** as the new algorithm

The implementation is written in Python and is developed from scratch for learning and demonstration purposes.

## Selected Topics
### Data Structure
**Binary Heap**

### Algorithm
**Heap Sort**

## Binary Heap
A binary heap is a complete binary tree usually implemented using an array.

This project implements the heap using a Python list.  
The heap supports the following operations:
- Push
- Pop
- Peek
- Heapify

The implementation can represent:
- Max-heap
- Min-heap

## Heap Sort
Heap sort works by:
1. Building a heap from the input data
2. Repeatedly removing the top element
3. Producing sorted output

This project demonstrates heap sort in both:
- Ascending order
- Descending order

## Complexity
- Building a heap: **O(n)**
- Heap sort: **O(n log n)**

## Applications
Binary heaps and heap sort are useful in:
- Priority queues
- Task scheduling
- Data ordering
- Efficient sorting

## File Structure
- `heap.py` - binary heap implementation
- `sorting.py` - heap sort implementation
- `demo.py` - demonstration program
- `README.md` - task overview

## How to Run
Open a terminal in the project root directory and run:

```bash
python -m task2.demo
