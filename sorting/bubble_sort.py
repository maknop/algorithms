class BubbleSort:
    """
    Implementation of the Bubble sort algorithm.

    Running Time: O(N log N)
    """
    def __init__(self, lst):
        self._lst = lst

    def sort(self, lst):
        for i in range(0, len(lst) - 1): 
            for j in range(0, len(lst) - 1 - i):  
                if lst[j] > lst[j + 1]:    
                    lst[j], lst[j + 1] = lst[j + 1], lst[j] 
                print(lst)    
        return lst  