from __future__ import annotations

from typing import Generic, Optional, Self, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(
        self,
        value: T,
    ) -> None:
        self._element = value
        self._next = None

    def get_element(self) -> T:
        return self._element

    def set_value(self, value) -> None:
        self._element = value

    def get_next(self) -> Optional[Node[T]]:
        return self._next

    def set_next(self, node: Node[T]) -> None:
        self._next = node

    def __str__(self) -> str:
        return f"(value: {self._element} | next: {self._next})"


class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self._size = 0
        self._head = None
        self._tail = None

    def push_front(self, value: T) -> None:
        node = Node(value)

        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node._next = self._head
            self._head = node
        self._size += 1

    def push_back(self, value: T) -> None:
        node = Node(value)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
            self._tail = node
        self._size += 1

    def pop_back(self) -> Optional[Node[T]]:
        if self.is_empty():
            return None

        if self._size == 1:
            tmp = self._head
            self._head = None
            self._tail = None
            self._size -= 1
            return tmp

        curr = self._head
        # traverse until current.next is the tail (we're at the penultimate node)
        while curr is not None and curr._next != self._tail:
            curr = curr._next

        tmp = self._tail
        # we need to validate this again (python compiler **sucks**)
        if curr:
            curr._next = None
        self._tail = curr
        self._size -= 1
        return tmp

    def pop_front(self) -> Optional[Node[T]]:
        head = self._head
        if head is not None:
            self._head = head._next
            head._next = None
            self._size -= 1
        return head

    def is_empty(self) -> bool:
        return True if self._size == 0 else False

    def front(self) -> Optional[Node[T]]:
        return self._head

    def back(self):
        return self._tail

    def contains(self, value: T) -> bool:
        curr = self._head
        while curr is not None:
            if curr.get_element() == value:
                return True
            curr = curr._next
        return False

    def len(self) -> int:
        return self._size

    def append(self, other: Self):
        if self.is_empty():
            return other

        if self._tail is not None:
            self._tail._next = other._head

    #  TODO: add `from`

    def __str__(self) -> str:
        return self._head.__str__()
