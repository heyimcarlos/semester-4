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
            node._next = self._tail
            self._tail._next = node
        self._size += 1

    def push_back(self, value: T) -> None:
        node = Node(value)
        if self._tail is None:
            node._next = node
            self._tail = node
        else:
            node._next = self._tail._next
            self._tail._next = node
            self._tail = node
        self._size += 1

    def is_empty(self) -> bool:
        return True if self._size == 0 else False

    def clone(self):
        cll = CircularlyLinkedList()
        if self.is_empty():
            return cll

        if self._tail:
            head = self._tail._next
            if head:
                cll.push_front(head.get_element())
                curr = self._tail._next

                for _ in range(self._size - 1):
                    if curr:
                        cll.push_back(curr.get_element())
                        curr = curr._next
                return cll

    def __str__(self) -> str:
        elements = []
        if self._tail:
            curr = self._tail._next
            while curr and curr != self._tail:
                elements.append(str(curr.get_element()))
                curr = curr._next
        return " -> ".join(elements) if elements else "[]"


if __name__ == "__main__":
    cll = CircularlyLinkedList()
    cll.push_back(1)
    cll.push_back(2)
    cll.push_back(3)

    cloned_cll = cll.clone()
    print(cll == cloned_cll)
    print(f"cll {cll}")
    print(f"cloned {cloned_cll}")
