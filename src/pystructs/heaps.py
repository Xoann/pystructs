from typing import Any, Dict
from abc import ABC, abstractmethod


class Heap(ABC):
    def __init__(self, array: list[Any] = None) -> None:
        if array is None:
            self.heap = []
            self.positions = {}
        else:
            self.positions = {}
            self.build_max_heap(array)

    def __str__(self):
        if not self.heap:
            return "Heap is empty"

        def print_tree(index, level):
            tree_str = ""
            if index < len(self.heap):
                tree_str += print_tree(2 * index + 2, level + 1)
                tree_str += "  " * level + str(self.heap[index]) + "\n"
                tree_str += print_tree(2 * index + 1, level + 1)
            return tree_str

        return print_tree(0, 0)

    def build_max_heap(self, array) -> None:
        self.heap = []
        for item in array:
            new_heap_node = HeapNode(item, item)
            self.heap.append(new_heap_node)
            self.positions[item] = len(self.heap) - 1

        n = (len(self.heap) - 1) // 2
        for i in range(n, -1, -1):
            self.bubble_down(i)

    def insert(self, item: Any, priority=None) -> None:
        if priority is None:
            priority = item

        new_heap_node = HeapNode(item, priority)
        self.positions[item] = len(self.heap)
        self.heap.append(new_heap_node)
        self.bubble_up(len(self.heap) - 1)

    def set_priority(self, item: int, priority: int) -> None:
        if item not in self.positions:
            raise ValueError("Item in not in heap")
        self.heap[self.positions[item]].priority = priority
        self.bubble_up(self.positions[item])

    @abstractmethod
    def bubble_up(self, i: int) -> None:
        pass

    @abstractmethod
    def bubble_down(self, i: int) -> None:
        pass


class HeapNode:

    def __init__(self, value: Any, priority) -> None:
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority

    def __str__(self) -> str:
        return str(self.value)


class MaxHeap(Heap):
    heap: list[Any]
    positions: Dict[int, Any]

    def bubble_up(self, i: int) -> None:
        if i == 0:
            return

        parent_index = (i - 1) // 2

        while i > 0 and self.heap[i] >= self.heap[parent_index]:
            self.heap[i], self.heap[parent_index] = self.heap[parent_index], self.heap[i]

            self.positions[self.heap[i].value], self.positions[self.heap[parent_index].value] \
                = self.positions[self.heap[parent_index].value], self.positions[self.heap[i].value]

            i = parent_index
            parent_index = (i - 1) // 2

    def bubble_down(self, i: int) -> None:
        n = len(self.heap)
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2
        largest = i

        if left_child_index < n and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < n and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]

            self.positions[self.heap[i].value], self.positions[self.heap[largest].value] \
                = self.positions[self.heap[largest].value], self.positions[self.heap[i].value]

            self.bubble_down(largest)

    def extract_max(self) -> Any:
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.positions[self.heap[0]] = 0
        heap_max = self.heap.pop()
        self.bubble_down(0)
        return heap_max.value

    def remove(self, item: Any) -> None:
        pass

    def max(self) -> Any:
        return self.heap[0]



