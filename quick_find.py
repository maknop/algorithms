class QuickFind:
    def __init__(self, n):
        """
        Check if two objects are in the same component.

        @param n: The length of the list
        """
        self.connected_components = [x for x in range(n)]

    def connected(self, p, q):
        """
        Replace components containing two objects with
        their union.

        @param p: Value to be changed.
        @param q: Value to change to.
        """
        return self.connected_components[p] == self.connected_components[q]

    def union(self, p, q):
        """
        Check if two objects are in the same component.

        
        @param p: Value to be changed.
        @param q: Value to change to.
        """
        for x in self.connected_components:
            if self.connected_components[x] == p:
                self.connected_components[x] = q

        return self.connected_components

    def __str__(self):
        print(self.connected_components)
        

if __name__ == '__main__':
    test = QuickFind(5)
    print(test.union(2, 1))
    