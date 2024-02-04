from typing import Any, Optional, Iterable, Callable


class Node:
    """
    Node
    """
    value: Any
    next: Optional['Node']

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        elements = []
        if self.next is None:
            return str(self.value)
        curr = self
        while curr is not None:
            elements.append(str(curr.value))
            curr = curr.next

        return ' -> '.join(elements)


def is_list(other: Any) -> bool:
    return isinstance(other, LinkedList) or isinstance(other, list)


def is_iterable(other: Any) -> bool:
    try:
        iter(other)
        return True
    except TypeError:
        return False


class LinkedList:
    """
    A linked list
    """
    head: Optional[Node]
    _length: int

    def __init__(self, lst: Iterable = None):
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
        if self.head is None:
            return "None"
        elements = [str(element) for element in self]
        return ' -> '.join(elements)

    def __repr__(self) -> str:
        if self.head is None:
            return "None"
        elements = [str(element) for element in self]
        return ' -> '.join(elements)

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, index: int) -> 'LinkedList':
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
        return LinkedListIterator(self.head, return_nodes, return_prev)

    def __contains__(self, item: Any) -> bool:
        for element in self:
            if element == item:
                return True
        return False

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, LinkedList) and not isinstance(other, list):
            return False
        if len(self) != len(other):
            return False

        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, LinkedList) and not isinstance(other, list):
            return True
        if len(self) != len(other):
            return True

        for i in range(len(self)):
            if self[i] != other[i]:
                return True
        return False

    def __lt__(self, other: Any) -> bool:
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
        self.insert(len(self), value)

    def remove(self, value: Any) -> None:
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

    def pop(self, index: int = -1) -> Any:
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
        self.head = None
        self._length = 0

    def index(self, value: Any, start: int = 0, end: int = None) -> int:
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
        count = 0
        for item in self:
            if item == value:
                count += 1
        return count

    def extend(self, other: Iterable) -> None:
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
        return LinkedList(self)

    def __add__(self, other: Any) -> 'LinkedList':
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
        raise TypeError(f"unsupported operand type(s) for -: '{type(self).__name__}' and '{type(other).__name__}'")

    def __mul__(self, other: Any) -> 'LinkedList':
        if not isinstance(other, int):
            raise TypeError(f"can't multiply sequence by non-int of type '{type(other).__name__}'")

        new_linked_list = LinkedList()
        for _ in range(other):
            for item in self:
                new_linked_list.append(item)
        return new_linked_list

    def __truediv__(self, other: Any) -> None:
        raise TypeError(f"unsupported operand type(s) for /: '{type(self).__name__}' and '{type(other).__name__}'")

    def __floordiv__(self, other: Any) -> None:
        raise TypeError(f"unsupported operand type(s) for //: '{type(self).__name__}' and '{type(other).__name__}'")

    def __mod__(self, other: Any) -> None:
        raise TypeError(f"unsupported operand type(s) for %: '{type(self).__name__}' and '{type(other).__name__}'")

    def __pow__(self, power: Any, modulo=None) -> None:
        raise TypeError(f"unsupported operand type(s) for ** or pow(): '{type(self).__name__}' and"
                        f" '{type(power).__name__}'")

    def __round__(self, n=None) -> None:
        raise TypeError(f"unsupported operand type(s) for round(): '{type(self).__name__}'")

    def __enter__(self) -> None:
        raise TypeError(f"'{type(self).__name__}' object does not support the context manager protocol")

    def __bool__(self) -> bool:
        return self.head is not None

    def _get_slice(self, start, stop, step) -> 'LinkedList':
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
        self._merge_sort(self.head, key=key, reverse=reverse)

    @staticmethod
    def _find_middle(head: Node) -> Node:
        slow = head
        fast = head

        prev_slow = None

        while fast is not None and fast.next is not None:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        return prev_slow if prev_slow else head


class LinkedListIterator:
    def __init__(self, head: Optional[Node], return_nodes: bool, return_prev: bool) -> None:
        self.current = head
        self.prev = None
        self.return_nodes = return_nodes or return_prev
        self.return_prev = return_prev

    def __iter__(self) -> 'LinkedListIterator':
        return self

    def __next__(self) -> Any:
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
