from typing import Any, Optional, Iterable, Callable


class Node:
    """
    Node used in linked lists

    Instance Attributes:
     - value (Any): value stored in the node
     - next (Optional[Node]): next node or None if there is no next node
    """
    value: Any
    next: Optional['Node']

    def __init__(self, value: Any) -> None:
        """
        Constructor for Node class

        :param value: value stored in node
        """
        self.value = value
        self.next = None

    def __str__(self) -> str:
        """
        String representation of node, prints similarly to linked lists

        :return: string representation of node chain
        """
        elements = []
        if self.next is None:
            return str(self.value)
        curr = self
        while curr is not None:
            elements.append(str(curr.value))
            curr = curr.next

        return ' -> '.join(elements)


def is_list(other: Any) -> bool:
    """
    Checks if other is a valid list type

    :param other: other to be checked
    :return: returns whether other is a valid list type
    """
    return isinstance(other, LinkedList) or isinstance(other, list)


def is_iterable(other: Any) -> bool:
    """
    Checks if other is iterable

    :param other: other to be checked
    :return: returns whether other is iterable
    """
    try:
        iter(other)
        return True
    except TypeError:
        return False


class LinkedList:
    """
    A linked list

    Instance Attributes:
     - head: The head of the linked list
     - _length: The length of the linked list
    """
    head: Optional[Node]
    _length: int

    def __init__(self, lst: Iterable = None):
        """
        Constructor for LinkedList class

        :param lst: Optional list of elements to instantiate linked list
        """
        self._length = 0
        if lst is None:
            self.head = None
            return
        curr = None

        for item in lst:
            node = Node(item)
            if curr is None:
                self.head = node
                self._length += 1
            else:
                curr.next = node
                self._length += 1
            curr = node

    def __str__(self) -> str:
        """
        String representation of the linked list

        :return: string representation of the linked list
        """
        if self.head is None:
            return "None"
        elements = [str(element) for element in self]
        return ' -> '.join(elements)

    def __repr__(self) -> str:
        """
        String representation of the linked list

        :return: string representation of the linked list
        """
        if self.head is None:
            return "None"
        elements = [str(element) for element in self]
        return ' -> '.join(elements)

    def __len__(self) -> int:
        """
        Gets the length of the linked list

        :return: length of the linked list
        """
        return self._length

    def __getitem__(self, index: int) -> 'LinkedList':
        """
        Index into linked list and return it

        :param index: index to fetch element from
        :return: returns value at index in the linked list
        """
        if isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            return self._get_slice(start, stop, step)
        if index < 0 or index >= self._length:
            raise IndexError

        i = 0
        for item in self:
            if i == index:
                return item
            i += 1

    def __setitem__(self, index: int, value: Any) -> None:
        """
        Sets value at index in the linked list to the given value

        :param index: index of element to change
        :param value: value to be set
        :return: none
        """
        if index < 0 or index >= self._length:
            raise IndexError

        if index == 0:
            if self.head is None:
                self.head = Node(value)
            else:
                node = Node(value)
                node.next = self.head.next
                self.head = node
            return

        i = 0
        prev = None
        curr = self.head
        for _ in self:
            if i == index:
                node = Node(value)
                prev.next = node
                if curr.next is not None:
                    node.next = curr.next
                else:
                    node.next = None

            prev = curr
            curr = curr.next
            i += 1

    def __iter__(self, return_nodes: bool = False, return_prev: bool = False) -> 'LinkedListIterator':
        """
        Iterates through self, used in for loops
        for element in linked_list():

        if return_nodes is True, the value returned is the nodes of self
        for node in linked_list.__iter__(return_nodes=True):

        if return_prev is True, the value returned is a tuple containing (curr, prev) nodes
        for curr, prev in linked_list.__iter__(return_prev=True):

        :param return_nodes: whether to return the nodes of self instead of the values
        :param return_prev: whether to also return the previous node in self
        :return: returns a linked list iterator that iterates through the linked list
        """
        return LinkedListIterator(self.head, return_nodes, return_prev)

    def __contains__(self, item: Any) -> bool:
        """
        Returns true if the given item is in self and false otherwise

        :param item: item to search for in linked list
        :return: whether the given item is in the linked list
        """
        for element in self:
            if element == item:
                return True
        return False

    def __eq__(self, other: Any) -> bool:
        """
        Checks whether other is equal to self

        :param other: other list to compare to
        :return: whether self and other are equal
        """
        if not isinstance(other, LinkedList) and not isinstance(other, list):
            return False
        if len(self) != len(other):
            return False

        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __ne__(self, other: Any) -> bool:
        """
        Checks whether list is not equal to self

        :param other: other list to compare to
        :return: whether self and other are not equal
        """
        if not isinstance(other, LinkedList) and not isinstance(other, list):
            return True
        if len(self) != len(other):
            return True

        for i in range(len(self)):
            if self[i] != other[i]:
                return True
        return False

    def __lt__(self, other: Any) -> bool:
        """
        Returns whether self is less than other

        :param other: other list to compare to
        :return: whether self is less than other
        """
        if not is_list(other):
            raise TypeError(f"'<' not supported between instances of {type(self).__name__} and {type(other).__name__}")

        if len(self) == len(other) == 0:
            return False
        if len(self) == 0:
            return True
        if len(other) == 0:
            return False
        return self[0] < other[0]

    def __le__(self, other: Any) -> bool:
        """
        Returns whether self is less than or equal to other

        :param other: other list to compare to
        :return: whether self is less than or equal to other
        """
        if not is_list(other):
            raise TypeError(f"'<=' not supported between instances of {type(self).__name__} and {type(other).__name__}")

        if len(self) == len(other) == 0:
            return True
        if len(self) == 0:
            return True
        if len(other) == 0:
            return False
        return self[0] <= other[0]

    def __gt__(self, other: Any) -> bool:
        """
        Returns whether self is greater than other

        :param other: other list to compare to
        :return: whether self is greater than other
        """
        if not is_list(other):
            raise TypeError(f"'>' not supported between instances of {type(self).__name__} and {type(other).__name__}")

        if len(self) == len(other) == 0:
            return False
        if len(self) == 0:
            return False
        if len(other) == 0:
            return True
        return self[0] > other[0]

    def __ge__(self, other: Any) -> bool:
        """
        Returns whether self is greater than or equal to other

        :raises TypeError: if other is not a list type
        :param other: other list to compare to
        :return: whether self is greater than or equal to other
        """
        if not is_list(other):
            raise TypeError(f"'>=' not supported between instances of {type(self).__name__} and {type(other).__name__}")

        if len(self) == len(other) == 0:
            return True
        if len(self) == 0:
            return False
        if len(other) == 0:
            return True
        return self[0] >= other[0]

    def insert(self, index: int, value: Any) -> None:
        """
        Inserts a value into self at index

        When index is greater than or equal to len(self), value is appended to self
        When index is negative the value is inserted at the abs(index)th position from the back of the list
        this value is clamped at 0

        Running time:
         - O(index)
         - O(1) at the beginning of the linked list

        :param index: int index to insert into the linked
        :param value: value to be inserted
        :return: None
        """
        new_node = Node(value)
        self._length += 1

        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        # Case index larger than list
        if index >= len(self):
            for _ in range(len(self) - 1):
                curr = curr.next
            curr.next = new_node
            return

        # Case index smaller than 0
        if index < 0:
            self.insert(max(0, index + len(self)), value)
            return

        # Default case index in bounds
        for _ in range(index - 1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def append(self, value: Any) -> None:
        """
        Appends a value to the end of self

        Running time:
         - O(n) where n = len(self)

        :param value: value to be appended
        :return: None
        """
        self.insert(len(self), value)

    def remove(self, value: Any) -> None:
        """
        Removes a value from self

        Running time:
        - O(n) where n = len(self)

        :raises ValueError: if the value is not in the list
        :param value: value to be removed from self
        :return: None
        """
        curr = self.head
        prev = None
        while curr is not None:
            if prev is None and curr.value == value:
                self.head = curr.next
                self._length -= 1
                return
            if curr.value == value:
                prev.next = curr.next
                self._length -= 1
                return
            prev = curr
            curr = curr.next
        raise ValueError("LinkedList.remove(value): value not in list")

    def pop(self, index: int = 0) -> Any:
        """
        Remove and return item at index.

        Index is 0 by default removing from the beginning of the list.

        Running Time:
         - O(index)
         - O(1) at the beginning of the linked lit

        :raises IndexError: if self is empty or index is out of range
        :param index: index to pop from self
        :return: item that was popped
        """
        if self.head is None:
            raise IndexError("pop from empty list")
        if index >= len(self) or -index > len(self):
            raise IndexError("pop index out of range")
        if index == 0:
            popped = self.head.value
            self.head = self.head.next
            self._length -= 1
            return popped

        if index < 0:
            index += len(self)
        i = 0
        curr = self.head
        prev = None
        while curr is not None:
            if i == index:
                popped = curr.value
                prev.next = curr.next
                self._length -= 1
                return popped
            prev = curr
            curr = curr.next
            i += 1

    def clear(self) -> None:
        """
        Clear the linked

        :return: None
        """
        self.head = None
        self._length = 0

    def index(self, value: Any, start: int = 0, end: int = None) -> int:
        """
        Return the index of value in self[start:end]

        :raises ValueError: if value is not in self[start:end]
        :param value: value to search for
        :param start: starting index to look from
        :param end: ending index to stop searching from (non-inclusive)
        :return: index of value
        """
        if end is None:
            end = len(self)

        index = 0
        curr = self.head
        while curr is not None:
            if curr.value == value and start <= index < end:
                return index
            index += 1
            curr = curr.next
        raise ValueError(f"{value} is not in list")

    def count(self, value: Any) -> int:
        """
        Return the number of occurrences of value in self

        :param value: value to count in self
        :return: number of occurrences of value in self
        """
        count = 0
        for item in self:
            if item == value:
                count += 1
        return count

    def extend(self, other: Iterable) -> None:
        """
        Extend the linked list with the values of other

        :raises TypeError: if other is not iterable
        :param other: iterable to extend self by
        :return: None
        """
        if not is_iterable(other):
            raise TypeError(f"'{type(other).__name__}' object is not iterable")

        if self.head is None:
            i = 0
            curr = None
            for item in other:
                node = Node(item)
                if i == 0:
                    self.head = node
                    curr = node
                else:
                    curr.next = node
                    curr = node
                    self._length += 1
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        for item in other:
            node = Node(item)
            curr.next = node
            curr = node
            self._length += 1

    def reverse(self) -> None:
        """
        Reverse self

        :return: None
        """
        if self.head is None:
            return

        curr = self.head
        prev = None
        while curr is not None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        self.head = prev

    def copy(self) -> 'LinkedList':
        """
        Return a copy of self

        :return: new linked list identical to self
        """
        return LinkedList(self)

    def __add__(self, other: Any) -> 'LinkedList':
        """
        Return a new linked list with the values of self concatenated with other

        :raises TypeError: if other is not a list type
        :param other: list to add with self
        :return: new linked list with values of self concatenated with other
        """
        if not is_list(other):
            raise TypeError(f"Can only concatenate list or {type(self).__name__} (not \"{type(other).__name__}\") to "
                            f"{type(self).__name__}")

        new_linked_list = LinkedList()
        for item in self:
            new_linked_list.append(item)
        for item in other:
            new_linked_list.append(item)
        return new_linked_list

    def __sub__(self, other: Any) -> None:
        """
        This operation is not supported for linked lists

        :raises TypeError: this operation is not supported
        """
        raise TypeError(f"unsupported operand type(s) for -: '{type(self).__name__}' and '{type(other).__name__}'")

    def __mul__(self, other: Any) -> 'LinkedList':
        """
        Return a new linked list with the values from self repeated other times.

        :param other: Number of times to repeat self in the new list
        :return: new linked list with the values from self repeated other times
        """
        if not isinstance(other, int):
            raise TypeError(f"can't multiply sequence by non-int of type '{type(other).__name__}'")

        new_linked_list = LinkedList()
        for _ in range(other):
            for item in self:
                new_linked_list.append(item)
        return new_linked_list

    def __truediv__(self, other: Any) -> None:
        """
        This operation is not supported for linked lists

        :raises TypeError: this operation is not supported
        """
        raise TypeError(f"unsupported operand type(s) for /: '{type(self).__name__}' and '{type(other).__name__}'")

    def __floordiv__(self, other: Any) -> None:
        """
        This operation is not supported for linked lists

        :raises TypeError: this operation is not supported
        """
        raise TypeError(f"unsupported operand type(s) for //: '{type(self).__name__}' and '{type(other).__name__}'")

    def __mod__(self, other: Any) -> None:
        """
        This operation is not supported for linked lists

        :raises TypeError: this operation is not supported
        """
        raise TypeError(f"unsupported operand type(s) for %: '{type(self).__name__}' and '{type(other).__name__}'")

    def __pow__(self, power: Any, modulo=None) -> None:
        """
        This operation is not supported for linked lists

        :raises TypeError: this operation is not supported
        """
        raise TypeError(f"unsupported operand type(s) for ** or pow(): '{type(self).__name__}' and"
                        f" '{type(power).__name__}'")

    def __round__(self, n=None) -> None:
        """
        This operation is not supported for linked lists

        :raises TypeError: this operation is not supported
        """
        raise TypeError(f"unsupported operand type(s) for round(): '{type(self).__name__}'")

    def __enter__(self) -> None:
        """
        This operation is not supported for linked lists

        :raises TypeError: this operation is not supported
        """
        raise TypeError(f"'{type(self).__name__}' object does not support the context manager protocol")

    def __bool__(self) -> bool:
        """
        Return self's bool conversion, false if head is None and true otherwise

        :return: whether self is empty
        """
        return self.head is not None

    def _get_slice(self, start, stop, step) -> 'LinkedList':
        """
        Helper that returns a new linked list sliced from self using start, stop and step.

        :param start: index to start slice
        :param stop: index to end slice (non-inclusive)
        :param step: step of slice
        :return: new linked list sliced from self
        """
        start = 0 if start is None else start
        stop = len(self) if stop is None else stop
        step = 1 if step is None else step

        new_list = LinkedList()
        i = 0
        curr = None

        if step < 0:
            new_list = self._get_slice(start, stop, 1)
            new_list.reverse()
            return new_list._get_slice(None, None, abs(step))

        for item in self:
            if i < start or (i - start) % step != 0:
                i += 1
                continue
            if i >= stop:
                break
            node = Node(item)
            if curr is None:
                new_list.head = node
                new_list._length += 1
            else:
                curr.next = node
                new_list._length += 1
            curr = node
            i += 1

        return new_list

    def _merge_sort(self, head: Node, key: Callable, reverse) -> None:
        """
        Helper that uses merge sort to sort the linked list in ascending order.

        If a key function is given, apply it once to each node value and sort them.

        The reverse flag can be set to sort in descending order.

        :param head: head of list to sort
        :param key: callable to sort values by
        :param reverse: flag to sort in descending order
        :return: None
        """
        if head is None or head.next is None:
            return
        middle = self._find_middle(head)
        left = head
        right = middle.next
        middle.next = None

        self._merge_sort(left, key, reverse)
        self._merge_sort(right, key, reverse)

        curr = left
        if self.head is None:
            self.head = left
        else:
            while curr.next:
                curr = curr.next
            curr.next = right

        self._merge(left, right, key, reverse)

    @staticmethod
    def _merge(left: Node, right: Node, key: Callable, reverse: bool) -> None:
        """
        Static helper to merge two sorted linked lists into one sorted linked list
        Note this method takes in nodes and not linked list as the sorting is in-place

        :param left: left head node
        :param right: right head node
        :param key: key to sort values by
        :param reverse: flag to sort in descending order
        :return: None
        """
        while left is not None and right is not None:
            if key:
                if ((not reverse and key(left.value) <= key(right.value)) or
                        (reverse and key(left.value) >= key(right.value))):
                    left = left.next
                else:
                    left.value, right.value = right.value, left.value
                    right = right.next
            else:
                if ((not reverse and left.value <= right.value) or
                        (reverse and left.value >= right.value)):
                    left = left.next
                else:
                    left.value, right.value = right.value, left.value
                    right = right.next

    def sort(self, key: Callable = None, reverse: bool = False) -> None:
        """
        Sort the list in ascending order.

        If a key function is given, apply it once to each node value and sort them.

        The reverse flag can be set to sort in descending order.

        :param key: callable to sort values by
        :param reverse: flag to sort in descending order
        :return: None
        """
        self._merge_sort(self.head, key=key, reverse=reverse)

    @staticmethod
    def _find_middle(head: Node) -> Node:
        """
        Static helper function to find the middle of a linked list given a head node to search from

        :param head: head node to search for middle from
        :return: return node at index n // 2, where n is the length of the sub list self[head:]
        """
        slow = head
        fast = head

        prev_slow = None

        while fast is not None and fast.next is not None:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        return prev_slow if prev_slow else head


class LinkedListIterator:
    """
    LinkedList iterator used by LinkedList.__iter__() to iterate over all values in a linked list
    """
    def __init__(self, head: Optional[Node], return_nodes: bool, return_prev: bool) -> None:
        """
        Interator initialization method

        If return_nodes is True the iterator returns nodes instead of values.

        If return_previous is True the iterator returns 2 nodes instead of values in a tuple (curr, prev)

        :param head: head of list
        :param return_nodes: flag to return node instead of values
        :param return_prev: flag to also return previous node along with current node
        """
        self.current = head
        self.prev = None
        self.return_nodes = return_nodes or return_prev
        self.return_prev = return_prev

    def __iter__(self) -> 'LinkedListIterator':
        """
        Return self

        :return: self
        """
        return self

    def __next__(self) -> Any:
        """
        Return next item in iteration
        :return: next value, node, of curr-prev pair in linked list
        """
        if self.current is None:
            raise StopIteration
        else:
            value = self.current.value
            curr = self.current
            prev = self.prev

            self.prev = self.current
            self.current = self.current.next

            if self.return_prev:
                return curr, prev
            if self.return_nodes:
                return curr
            return value
