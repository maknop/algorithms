"""
Pytest: Testing library.
"""
from quick_find import QuickFind
import pytest


def test_empty_list():
    """
    This test will check if the list is not empty.
    """
    n_list = QuickFind(10)

    assert len(n_list.connected_components) != 0
    
def test_connected():
    """
    This function should check if two indexes are connected.

    @return False
    """
    n_list = QuickFind(10)

    assert n_list.connected(1, 4) == False

def test_union():
    n_list = QuickFind(5)

    assert n_list.union(2, 1) == [0, 1, 1, 3, 4]