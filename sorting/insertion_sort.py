class InsertionSort:
    """
    Implementation of the Insertion sort algorithm.

    Running Time: O(N^2)
    """
    def __init__(self, lst):
        self._lst = lst

    def sort(self, _lst):

        for i in range(len(_lst)):
            j = i   
            while j > 0 and _lst[j - 1] > _lst[j]: 
                temp = _lst[j - 1]  
                _lst[j - 1] = _lst[j] 
                _lst[j] = temp  
                j -= 1  
            i += 1  

              