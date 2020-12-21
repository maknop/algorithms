# Algorithms Practice

## Description
Purpose of this repository is to study various algorithms from a  
variety of sources:
- Coursera called [Algorithms, Part 1](https://www.coursera.org/learn/algorithms-part1).
- Runestone Academy's Data Structures and Algorithms Book titled "Problem Solving with Algorithms and Data Structures using Python"

## Types of Algorithms
- [Bubble Sort](/sorting/bubble_sort.py)
- [Insertion Sort](/sorting/insertion_sort.py)
- [Selection Sort](/sorting/selection_sort.py)
- [Binary Search](/search/binary_search.py)
- [Hash List](/other/hash_list.py)
- [Linked List](/other/linked_list.py)
- [Doubly Linked List](/other/doubly_linked_list.py)
- [Stack](/other/stack.py)
- [Queue](/other/queue.py)
- [Dequeue](/other/dequeue.py)

## Install Dependencies
Make sure you have pytest installed.
```
pip install pytest
```

## Run All Tests
```
pytest -v
```

## Run Tests By Algorithm
```
pytest test_quick_find.py -v
pytest test_hash_table.py -v
pytest test_insertion_sort.py -v
pytest test_selection_sort.py -v
pytest test_bubble_sort.py -v
pytest test_binary_search.py -v
```
