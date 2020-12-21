"""
Import bubble sort object.
Pytest: Testing library.
"""
from sorting.bubble_sort import BubbleSort
import pytest


def test_none_repeating():
    """
    Tests sorting success with non-repeating integers.
    """
    lst = [5, 6, 3, 8, 9, 2, 4]
    bubble = BubbleSort(lst)
    bubble.sort(lst)

    assert(bubble._lst == [2, 3, 4, 5, 6, 8, 9])

def test_duplicates():
    """
    Tests sorting success with duplicate integers. 
    """
    lst = [3, 9, 2, 3, 2, 7, 5, 2, 10]
    bubble = BubbleSort(lst)
    bubble.sort(lst)

    assert(bubble._lst == [2, 2, 2, 3, 3, 5, 7, 9, 10])

def test_negative_numbers():
    """
    Test sorting success with negative numbers. 
    """
    lst = [-5, -10, -4, 5, 3, -100, -50]
    bubble = BubbleSort(lst)
    bubble.sort(lst)

    assert(bubble._lst == [-100, -50, -10, -5, -4, 3, 5])