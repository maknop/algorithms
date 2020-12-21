class SelectionSort:
    def __init__():
            """
    Implementation of the Selection sort algorithm.

    Running Time: O(N^2)
    """
    def __init__(self, lst):
        self._lst = lst
    
    def sort(self, _lst):
        for i in range(len(_lst) - 1, -1, -1): 
            maxIndex = i 
            for j in range(i - 1, -1, -1): 
                print(_lst) 

                if _lst[j] > _lst[maxIndex]: 
                    maxIndex = j

            if maxIndex != i:
                _lst[maxIndex], _lst[i] = _lst[i], _lst[maxIndex]

        return _lst