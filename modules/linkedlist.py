"""
Butynets' Danylo
Python 3.8
"""


class Linked:
    """
    Represent a linked list.
    """
    def __init__(self):
        """
        (Linked) -> None
        Initialize new linked list.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        (Linked) -> int
        Return size of the linked list.
        :return: int
        """
        return self._size

    def head(self):
        """
        (Linked) -> LinkedNode or None
        Return head of the list.
        :return: LinkedNode or None
        """
        return self._head

    def add(self, item):
        """
        (Linked, object) -> None
        Add a new item to the end of the linked list.
        :param item: object
        :return: None
        """
        if self._head is None:
            self._head = LinkedNode(item)
            self._tail = self._head
        else:
            new = LinkedNode(item)
            self._tail.next = new
            self._tail = new
            self._size += 1

    def __iter__(self):
        """
        (Linked) -> _LinkedIter
        Iterate through linked list.
        :return: _LinkedIter
        """
        return _LinkedIter(self._head)

    def __str__(self):
        """
        (Linked) -> str
        Return string representation of the linked list.
        :return: str
        """
        st = ''
        node = self._head
        while node is not None:
            st += str(node.item) + ' -> '
            node = node.next
        return st[:-4]


class _LinkedIter:
    """
    Represent a linked list iterator.
    """
    def __init__(self, start):
        """
        (_LinkedIter, LinkedNode) -> None
        Initialize a new linked list iterator.
        :param start: LinkedNode
        """
        self._cur = start

    def __iter__(self):
        """
        (_LinkedIter) -> _LinkedIter
        Iterate through the list.
        :return: _LinkedIter
        """
        return self

    def __next__(self):
        """
        (_LinkedIter) -> object or exception
        Return the next item.
        """
        if self._cur is None:
            raise StopIteration
        else:
            res = self._cur.item
            self._cur = self._cur.next
            return res


class LinkedNode:
    """
    Represent a node in linked list.
    """
    def __init__(self, value):
        """
        (LinkedNode, object) -> None
        Initialize a node for linked link.
        :param value: object
        """
        self.item = value
        self.next = None

    def __str__(self):
        """
        (LinkedNode) -> str
        Return a node in string representation.
        :return: str
        """
        return str(self.item)
