from typing import Any, Optional


class Node:
    """
    Node
    """
    value: Any
    next: Optional['Node']

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None


def is_list(other: Any) -> bool:
    return isinstance(other, LinkedList) or isinstance(other, list)


class LinkedList:
    """
    A linked list
    """
    head: Optional[Node]
    _length: int

    def __init__(self, lst: list = None):
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

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, index: int) -> Node:
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

    def __iter__(self) -> 'LinkedListIterator':
        return LinkedListIterator(self.head)

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
        if not isinstance(other):
            raise TypeError(f"'<' not supported between instances of {type(self).__name__} and {type(other).__name__}")

        if len(self) == len(other) == 0:
            return False
        if len(self) == 0:
            return True
        if len(other) == 0:
            return False
        return self[0] < other[0]

    def __le__(self, other: Any) -> bool:
        if not isinstance(other):
            raise TypeError(f"'<=' not supported between instances of {type(self).__name__} and {type(other).__name__}")

        if len(self) == len(other) == 0:
            return True
        if len(self) == 0:
            return True
        if len(other) == 0:
            return False
        return self[0] <= other[0]

    def __gt__(self, other: Any) -> bool:
        if not isinstance(other):
            raise TypeError(f"'>' not supported between instances of {type(self).__name__} and {type(other).__name__}")

        if len(self) == len(other) == 0:
            return False
        if len(self) == 0:
            return False
        if len(other) == 0:
            return True
        return self[0] > other[0]

    def __ge__(self, other: Any) -> bool:
        if not isinstance(other):
            raise TypeError(f"'>=' not supported between instances of {type(self).__name__} and {type(other).__name__}")

        if len(self) == len(other) == 0:
            return True
        if len(self) == 0:
            return False
        if len(other) == 0:
            return True
        return self[0] >= other[0]

    # TODO: Implement negative index insertion
    def insert(self, index: int, value: Any) -> None:
        new_node = Node(value)

        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        self._length += 1
        curr = self.head
        # Case index larger than list
        if index >= len(self):
            for _ in range(len(self) - 1):
                curr = curr.next
            curr.next = new_node
            return

        # Case index smaller than 0

        # Default case index in bounds
        for _ in range(index - 1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node



class LinkedListIterator:
    def __init__(self, head: Optional[Node]) -> None:
        self.current = head

    def __iter__(self) -> 'LinkedListIterator':
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            value = self.current.value
            self.current = self.current.next
            return value

