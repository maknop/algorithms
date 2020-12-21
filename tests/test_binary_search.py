"""
Import binary search object.
Pytest: Testing library.
"""
from search.binary_search import BinarySearch
import pytest


def test_binary_search():
    lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    item = 5

    bSearch = BinarySearch(lst, item)
    bSearch.binary_search(lst, item)

    assert(bSearch.lst == 2)