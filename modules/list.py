"""
Butynets' Danylo
Python 3.8
"""


import ctypes


class List:
    """
    Represent an array/list.
    """
    def __init__(self, size):
        """
        (List, int) -> None
        Create new list.
        :param size: int
        """
        array = ctypes.py_object*size
        self._contents = array()
        self._size = size
        self.clear(None)

    def __len__(self):
        """
        (List) -> int
        Return size of the list.
        """
        return self._size

    def __getitem__(self, index):
        """
        (List, int) -> object
        Return element on given index
        """
        return self._contents[index]

    def __setitem__(self, index, value):
        """
        (List, int, object) -> None
        Set a new value the given index.
        """
        self._contents[index] = value

    def clear(self, value):
        """
        (List, object) -> None
        Set all the entries to the value.
        """
        for i in range(len(self)):
            self._contents[i] = value

    def __iter__(self):
        """
        (List) -> _ListIter
        Iterate through list.
        """
        return _ListIter(self._contents)

    def __str__(self):
        """
        (List) -> str
        Return string representation of the list.
        """
        st = '['
        for i in range(self._size):
            st += str(self[i]) + ', '
        return st[:-2] + ']'


class _ListIter:
    """
    Represent List iterator.
    """
    def __init__(self, arr):
        """
        (_ListIter, List) -> None
        Initialize new list iterator.
        """
        self._ref = arr
        self._index = 0

    def __iter__(self):
        """
        (_ListIter) -> _ListIter
        Iterate through the iterator.
        """
        return self

    def __next__(self):
        """
        (_ListIter) -> object or exception
        Return the next item.
        """
        if self._index < len(self._ref):
            item = self._ref[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
