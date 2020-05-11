"""
Butynets' Danylo
Python 3.8
"""


class Dict:
    """
    Represent a custom dictionary.
    """
    def __init__(self):
        """
        (Dict) -> None
        Initialize new dictionary.
        """
        self._content = list()
        self._size = 0

    def __len__(self):
        """
        (Dict) -> int
        Return the size of the Dict.
        :return: int
        """
        return self._size

    def __iter__(self):
        """
        (Dict) -> _DictIter
        Iterate through Dict's values.
        :return: _DictIter
        """
        return _DictIter(self._content)

    def keys(self):
        """
        (Dict) -> list
        Return list of Dict's keys.
        :return: list
        """
        keys = list()
        for node in self._content:
            keys.append(node.key())
        return keys

    def __setitem__(self, key, value):
        """
        (Dict, object, object) -> None
        Set given value to the given key and create
        key  if it is missing.
        :param key: mutable object
        :param value: object
        :return: None
        """
        if key not in self.keys():
            self._content.append(DictNode(key, value))
            self._size += 1
        else:
            for node in self._content:
                if key == node.key():
                    node.set_value(value)

    def __getitem__(self, item):
        """
        (Dict, object) -> object
        Get value from the given key.
        :param item: object(mutable)
        :return: object
        """
        assert item in self.keys(), "Key not found in dict."
        for node in self._content:
            if node.key() == item:
                return node.value()

    def __str__(self):
        """
        (Dict) -> str
        Return string representation of the Dict.
        :return: str
        """
        res = "["
        for key in self.keys():
            res = res + "(" + str(key)+": "+str(self[key])+")"
        return res + "]"


class _DictIter:
    """
    Represent Dict iterator.
    """
    def __init__(self, lst):
        """
        (_DictIter, list) -> None
        Initialize new dict iterator.
        :param lst: list
        """
        self._reflection = lst
        self._curr = 0

    def __iter__(self):
        """
        (_DictIter) -> _DictIter
        Iterate through the Dict.
        :return: _DictIter
        """
        return self

    def __next__(self):
        """
        (_DictIter) -> object or exception
        Return the next value of the Dict.
        :return: object or exception
        """
        if self._curr < len(self._reflection):
            entry = self._reflection[self._curr]
            self._curr += 1
            return entry.value()
        else:
            raise StopIteration


class DictNode:
    """
    Represent a node in a Dict.
    """
    def __init__(self, key, value):
        """
        Initialize Dict node with key and value.
        :param key: object
        :param value: object
        """
        self._key = key
        self._value = value

    def key(self):
        """
        Return the key of the node.
        :return: object
        """
        return self._key

    def value(self):
        """
        Return the value of the node.
        :return: object
        """
        return self._value

    def set_value(self, val):
        """
        Change the value of the node.
        :param val: object
        :return: None
        """
        self._value = val

    def __str__(self):
        """
        Return string representation of the node.
        :return: str
        """
        return f"({self._key}: {self._value})"
