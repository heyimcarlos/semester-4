from __future__ import annotations

from typing import Any, Optional


class Node:
    _value: Any
    _next: Optional[Node]
    _prev: Optional[Node]

    def __init__(
        self, value, prev: Optional[Node] = None, next: Optional[Node] = None
    ) -> None:
        self._value = value
        self._next = next
        self._prev = prev

    def get_value(self) -> Any:
        return self._value

    def set_value(self, value) -> None:
        self._value = value

    def get_next(self) -> Optional[Node]:
        return self._next

    def set_next(self, node: Node) -> None:
        self._next = node

    def get_prev(self) -> Optional[Node]:
        return self._prev

    def set_prev(self, node: Node) -> None:
        self._prev = node

    def __str__(self) -> str:
        # return f"({self._value}) -> ({"None" if self._next is None else self._next._value})"
        # return (
        return f"(prev: {self._prev} | value: {self._value} | next: {self._next})"
        # if self._prev is None
        # else f"(value: {self._value} | next: {self._next})"

    # )


class SinglyLinkedList:
    _head: Optional[Node]
    _tail: Optional[Node]
    _size: int

    def __init__(self) -> None:
        self._size = 0
        self._head = None
        self._tail = None
        pass

    def get_first(self) -> Any:
        if self._head is not None:
            return self._head._value

    def get_last(self) -> Any:
        if self._tail is not None:
            return self._tail.get_value()

    def push_front(self, value: Any) -> None:
        node = Node(value)

        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node._next = self._head
            self._head = node
        self._size = self._size + 1

    def push_back(self, value: Any) -> None:
        node = Node(value)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
        self._size += 1

    def is_empty(self) -> bool:
        return True if self._size == 0 else False

    def front(self) -> Optional[Node]:
        return self._head

    def back(self) -> Optional[Node]:
        return self._tail

    # define new (which creates a new instance of singlylinkedlist)
    # def new(self) -> SinglyLinkedList()

    def __str__(self) -> str:
        return self._head.__str__()


# singly_linked_list = SinglyLinkedList()
# singly_linked_list.push_front(1)
# singly_linked_list.push_front(2)
# singly_linked_list.push_front(3)
# singly_linked_list.push_front(4)
# singly_linked_list.push_front(5)
# singly_linked_list.push_back(0)
# print(singly_linked_list)


# header (head) and trailer (tail) are empty
# sentinel nodes:
class DoublyLinkedList:
    _header: Optional[Node]
    _trailer: Optional[Node]
    _size: int

    def __init__(self) -> None:
        self._header = Node(value=None, prev=None, next=None)
        self._trailer = Node(value=None, prev=self._header, next=None)
        self._header.set_next(self._trailer)
        self._size = 0

    #  TODO: implement `concatenate` (takes a doublylinkedlist and concats to the end of the current instance)
    def __str__(self) -> str:
        return self._header.__str__()


doubly_linked_list = DoublyLinkedList()
print(doubly_linked_list)
