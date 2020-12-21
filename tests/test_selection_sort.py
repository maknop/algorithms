"""
Import selection sort object.
Pytest: Testing library.
"""
from sorting.selection_sort import SelectionSort
import pytest


def test_none_repeating():
    """
    Tests sorting success with non-repeating integers.
    """
    lst = [5, 6, 3, 8, 9, 2, 4]
    selection = SelectionSort(lst)
    selection.sort(lst)

    assert(selection._lst == [2, 3, 4, 5, 6, 8, 9])

def test_duplicates():
    """
    Tests sorting success with duplicate integers. 
    """
    lst = [3, 9, 2, 3, 2, 7, 5, 2, 10]
    selection = SelectionSort(lst)
    selection.sort(lst)

    assert(selection._lst == [2, 2, 2, 3, 3, 5, 7, 9, 10])

def test_negative_numbers():
    """
    Test sorting success with negative numbers. 
    """
    lst = [-5, -10, -4, 5, 3, -100, -50]
    selection = SelectionSort(lst)
    selection.sort(lst)

    assert(selection._lst == [-100, -50, -10, -5, -4, 3, 5])