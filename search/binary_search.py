class BinarySearch:
    def __init__(self, lst, item):
        self.lst = lst
        self.item = item

    def rec_binary_search(self, lst, item):
        """
        Single interation of binary search where the middle value in
        the list is compared to the item we are searching for. If those
        values do not match, the list is sliced in half.

        Arguments:
            lst {[type]} -- [description]
            item {[type]} -- [description]
        """
        mid = len(lst) // 2

        if lst[mid] == item:
            return mid
        elif lst[mid] < item:
            rec_binary_search(lst[mid: len(lst)], item)
        elif lst[mid] > item:
            rec_binary_search(lst[0: mid], item)
        elif len(lst) == 1:
            return -1


    def binary_search(self, lst, item):
        """
        Calls the binary search algorithm recursively.

        Arguments:
            lst {Integer} -- Ordered list of integer values.
            item {Integer} -- Item that will be searched.
        """
        rec_binary_search(lst, item)
