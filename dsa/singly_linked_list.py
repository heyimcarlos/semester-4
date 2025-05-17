from __future__ import annotations

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    _element: T
    _next: Optional[Node]

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
    _head: Optional[Node[T]]
    _tail: Optional[Node[T]]
    _size: int

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

        curr = self._head
        while curr is not None:
            if curr._next is None or self._tail is None:
                return None

            # this is matching the element, not the memory address.
            if curr._next.get_element() == self._tail.get_element():
                tail = self._tail
                curr._next = None
                self._tail = curr
                self._size -= 1
                return tail
            curr = curr._next
        return curr

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

    def back(self) -> Optional[Node[T]]:
        return self._tail

    #  TODO: add `from`, `pop_back`, `pop_front`, `append/concat`, `contains`
    # define new (which creates a new instance of singlylinkedlist)
    # def new(self) -> SinglyLinkedList()

    def __str__(self) -> str:
        return self._head.__str__()


singly_linked_list = SinglyLinkedList()
singly_linked_list.push_front(1)
singly_linked_list.push_front(2)
singly_linked_list.push_front(3)
singly_linked_list.push_front(4)
singly_linked_list.push_front(5)
singly_linked_list.push_back(0)
print(f"{singly_linked_list}")
pf = singly_linked_list.pop_front()
print(f"pop front: {singly_linked_list}")
pb = singly_linked_list.pop_back()
print(f"pop back: {singly_linked_list}")
print(f"pop back: {pb}")
# print(f"last {singly_linked_list.back()}")
