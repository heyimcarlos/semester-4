from __future__ import annotations

import copy
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
        next_repr = "None"
        if self._next:
            next_repr = f"{self._next.get_element()}"  # Just show the next element

        return f"(value: {self._element} | next: {next_repr})"


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

    #  NOTE: Assignment 1
    # Exercise 1
    def swap(self, node1: Node[T], node2: Node[T]):
        if self.is_empty():
            return
        if node1 == node2:
            return
        if self._size == 2:
            node1._next = node2._next
            node2._next = node1
            self._head = node2
            self._tail = node1
            return

        # node1 predecessor
        pred1 = None
        curr = self._head
        while curr is not None and curr != node1:
            pred1 = curr
            curr = curr._next

        # node2 predecessor
        pred2 = None
        curr = self._head
        while curr is not None and curr != node2:
            pred2 = curr
            curr = curr._next

        # if pred1 is none, node1 is the head, so node2 should be the new head
        if pred1 is None:
            self._head = node2
        # else node1 predecessor should be node2
        else:
            pred1._next = node2

        # if pred2 is none, node2 is the head, so node1 should be the new head
        if pred2 is None:
            self._head = node1
        # else node2 predecessor should be node1
        else:
            pred2._next = node1

        if node1._next == node2:
            tmp = node2._next
            node1._next = tmp
            node2._next = node1
        elif node2._next == node1:
            tmp = node1._next
            node2._next = tmp
            node1._next = node2
        else:
            tmp = node1._next
            node1._next = node2._next
            node2._next = tmp

        if node1._next is None:
            self._tail = node1
        elif node2._next is None:
            self._tail = node2

    def __str__(self) -> str:
        elements = []
        curr = self._head
        while curr:
            elements.append(str(curr.get_element()))
            curr = curr._next
        return " -> ".join(elements) if elements else "[]"


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    ll.push_back(5)

    print("Original list:")
    print(ll)

    # Get references to nodes for swapping
    node_to_swap1 = None
    node_to_swap2 = None
    curr = ll._head
    while curr:
        if curr.get_element() == 2:
            node_to_swap1 = curr
        if curr.get_element() == 4:
            node_to_swap2 = curr
        curr = curr._next

    print("\nSwapping nodes with elements 2 and 4 (non-adjacent):")
    ll.swap(node_to_swap1, node_to_swap2)
    print(ll)

    # Reset list and try adjacent swap
    ll = SinglyLinkedList()
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    ll.push_back(5)

    node_to_swap1 = None
    node_to_swap2 = None
    curr = ll._head
    while curr:
        if curr.get_element() == 2:
            node_to_swap1 = curr
        if curr.get_element() == 3:
            node_to_swap2 = curr
        curr = curr._next

    print("\nSwapping nodes with elements 2 and 3 (adjacent, node1 before node2):")
    ll.swap(node_to_swap1, node_to_swap2)
    print(ll)

    # Reset list and try adjacent swap where node2 comes before node1
    ll = SinglyLinkedList()
    ll.push_back(1)
    ll.push_back(3)
    ll.push_back(2)
    ll.push_back(4)
    ll.push_back(5)

    node_to_swap1 = None
    node_to_swap2 = None
    curr = ll._head
    while curr:
        if curr.get_element() == 3:
            node_to_swap1 = curr
        if curr.get_element() == 2:
            node_to_swap2 = curr
        curr = curr._next

    print("\nSwapping nodes with elements 3 and 2 (adjacent, node2 before node1):")
    ll.swap(node_to_swap1, node_to_swap2)
    print(ll)

    # Reset list and try swapping head and a middle node
    ll = SinglyLinkedList()
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)

    node_to_swap1 = ll._head
    node_to_swap2 = None
    curr = ll._head
    while curr:
        if curr.get_element() == 3:
            node_to_swap2 = curr
        curr = curr._next

    print("\nSwapping head (1) and node with element 3:")
    ll.swap(node_to_swap1, node_to_swap2)
    print(ll)

    # Reset list and try swapping head and adjacent node
    ll = SinglyLinkedList()
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)

    node_to_swap1 = ll._head
    node_to_swap2 = ll._head._next

    print("\nSwapping head (1) and adjacent node (2):")
    ll.swap(node_to_swap1, node_to_swap2)
    print(ll)

    # Reset list and try swapping tail and a middle node
    ll = SinglyLinkedList()
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)

    node_to_swap1 = ll._tail
    node_to_swap2 = ll._head._next  # Node with element 2

    print("\nSwapping tail (3) and middle node (2):")
    ll.swap(node_to_swap1, node_to_swap2)
    print(ll)
