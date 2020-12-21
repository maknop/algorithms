"""
TODO: Documentation for imports
"""


class HashTable:
    def __init__(self, size):
        """
        Object init function.
        """
        self.slots = [None for x in range(size)]
        self.size = size

    def hash(self, value):
        """
        Adds value to location in list by taking the modulus
        of the value and the length of the list.
        """
        self.slots.insert(value % self.size, value)

    def get_value(self, value):
        """
        Returns the location of the value given.
        """
        pass

    def rehash_cluster(self):
        """
        Collision Resolution - Clustering: If hash location is already 
        taken, this functionwill search sequentially until an available 
        slot is open.
        """
        pass

    def rehash_chaining(self):
        """
        Collision Resolution - Chaining: IF 
        """
        pass
