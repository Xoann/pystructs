from linked_list import LinkedList
from typing import Any, List


class Stack:
    stack: List

    def __init__(self) -> None:
        self.stack = []

    def push(self, item: Any) -> None:
        self.stack.append(item)

    def pop(self) -> Any:
        return self.stack.pop()

    def peek(self) -> Any:
        return self.stack[len(self.stack) - 1]

    def __len__(self):
        return len(self.stack)


class Queue:
    queue: LinkedList

    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def peek(self) -> Any:
        return self.queue[len(self.queue) - 1]

    def is_empty(self) -> bool:
        return len(self.queue) == 0

class PriorityQueue(Queue):
    queue: LinkedList

