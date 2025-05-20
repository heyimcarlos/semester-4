from __future__ import annotations

from typing import Generic, Optional, TypeVar

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


# implement clone
class CircularlyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self._tail = None
        self._size = 0

    def push_front(self, value: T) -> None:
        node = Node(value)
        if self._tail is None:
            self._tail = node
            self._tail._next = self._tail
        else:
            node._next = self._tail._next
            self._tail._next = node

        self._size += 1

    def push_back(self, value: T) -> None:
        node = Node(value)
        if self._tail is None:
            self._tail = node
            self._tail._next = node
        else:
            node._next = self._tail._next
            self._tail._next = node
            self._tail = node
        self._size += 1

    def is_empty(self) -> bool:
        return True if self._size == 0 else False

    def clone(self):
        cll = CircularlyLinkedList()
        # return new empty list if the current is empty
        if self.is_empty():
            return cll

        if self._tail:
            head = self._tail._next
            if head:
                cll.push_back(head.get_element())
                curr = head._next
                # iterate size - 1 times, because the list already holds the head
                for _ in range(self._size - 1):
                    if curr:
                        cll.push_back(curr.get_element())
                        curr = curr._next
                return cll

    def __str__(self) -> str:
        if self.is_empty():
            return "[] (Circular)"
        elements = []
        if self._tail:
            curr = self._tail._next
            for _ in range(self._size):
                if curr:
                    elements.append(str(curr.get_element()))
                    curr = curr._next
        return " -> ".join(elements) + " -> (head)"


if __name__ == "__main__":
    cll = CircularlyLinkedList()
    cll.push_front(1)
    cll.push_front(2)
    cll.push_front(3)
    cll.push_back(4)
    cll.push_back(5)
    cll.push_back(6)

    cloned_cll = cll.clone()
    print(cll == cloned_cll)
    print(f"cll {cll}")
    print(f"cloned {cloned_cll}")
