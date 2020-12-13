"""
Import hash table object.
Pytest: Testing library.
"""
from hash_table import HashTable
import pytest


def test_hash():
    """
    Test for hash()
    """
    hash_table = HashTable(10)
    hash_table.hash(11)

    assert(hash_table.slots[1] == 11)

def test_get_value():
    """
    Test for get_value()
    """
    hash_table = HashTable(10)

    assert(hash_table.slots)

def test_rehash():
    """
    Test for rehash()
    """
    pass
    