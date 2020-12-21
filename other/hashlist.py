class HashList:
    def __init__(self, length):
        self.length = length
        self.data = [None] * self.length


    def hash_function(self, length, data):
        """
        Uses the modulus operator to find a location in the hashlist
        currently holding no value and returns that location.

        Arguments:
            length {Integer} -- Size of the hashlist.
            data {Integer} -- The hashlist we are storing data in.

        Returns:
            Integer -- the hashed value to store the data.
        """
        return data % length


    def rehash_function(self, prev, size):
        """
        If the hash function returns a location that currently holds
        a data item, the rehash function finds the next available,
        non-occupied location in the hashlist.

        Arguments:
            prev {Integer} -- Current location occupied by a data item.
            size {Integer} -- Size of the hashlist.

        Returns:
            [Integer] -- New location in the hashlist not occupied by a data item.
        """
        return (prev % self.length) + 1


    def put(self, item):
        """
        Adds a new item to the hashlist.

        Arguments:
            item {Integer} -- The item to add to the hashlist.
        """
        hash_location = self.hash_function(self.length, item)
        if self.data[hash_location] == None:
            self.data[hash_location] = item
        else:
            while self.data[hash_location] is not None:
                hash_location = self.rehash_function(hash_location, len(self.data))
                if self.data[hash_location] is None:
                    self.data[hash_location] = item
                    return
                else:
                    hash_location += 1
            self.data[hash_location] = item


    def __str__(self):
        """
        Returns the string representation of the hashlist.

        Returns:
            [Str] -- String representation of the hashlist.
        """
        return str(self.data)


    def contains(self, item):
        """
        Checks the hashlist for a specified data item.

        Arguments:
            item {Integer} -- Data item to add to the hashlist.
        """
        for x in self.data:
            if x == item:
                print("The item %s is in the list." % (item))
                return
        print("The item %s is NOT in the list." % (item))


test = HashList(9)
test.put(56)
test.put(29)
test.put(38)

print(test)

test.contains(56)
test.contains(2)
test.contains(38)