class SelectionSort:
    def __init__():
            """
    Implementation of the Selection sort algorithm.

    Running Time: O(N^2)
    """
    def __init__(self, lst):
        self._lst = lst
    
    def sort(self, _lst):
        for i in range(len(_lst) - 1, -1, -1):                         # O(n) - Interate over lst.
            maxIndex = i                                                # O(1) - Set value.
            for j in range(i - 1, -1, -1):                              # O(n) - Interate over lst.
                print(_lst)                                            # O(1) - Print statement.
                # Checking to see if element is the biggest.
                if _lst[j] > _lst[maxIndex]:                          # O(1) - Compares indices.
                    maxIndex = j                                        # O(1) - Set value.

            # Swap and puts item into it's place
            if maxIndex != i:                                           # O(1) - Check the max against the index.
                _lst[maxIndex], _lst[i] = _lst[i], _lst[maxIndex]   # O(1) - Set values.

        return _lst