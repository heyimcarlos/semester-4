from __future__ import annotations

from typing import Generic, TypeVar


class User:
    """this is a docstring, we use it for documentation"""

    # define constructor
    def __init__(self, name: str, age: int) -> None:
        """this docstring is scoped to the constructor"""

        self.name = name
        self.age = age
        self._name = name

    def log(self) -> None:
        """this docstring is scoped to a method"""
        print(f"{self.name} is {self.age} years old")
        print(f"self -> {self._name}")


class Admin(User):
    """Admin class inheriting from User"""

    def __init__(self, name: str, age: int, permissions: list) -> None:
        """this docstring is scoped to the constructor"""
        super().__init__(name, age)
        self._permissions = permissions


# user_one = User("John", 22)
# user_two = User("Doe", 25)
# users = [user_one, user_two]
# users_iter = users.__iter__()
# print(f"users_iter -> {users_iter.__next__().log()}")


admin_one = Admin("Jane", 30, ["read", "write", "deploy"])


# generics in python

T = TypeVar("T")


class GenericClass(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get_value(self) -> T:
        return self.value


# abstract classes in python

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self) -> None:
        pass


# interfaces in python


class InterfaceClass(ABC):
    @abstractmethod
    def interface_method(self) -> None:
        pass


# self-referencing classes

E = TypeVar("E")


class Item(Generic[E]):
    _element: E
    _item: Item[E]

    def __init__(self, element: E, item: Item[E]) -> None:
        self._element = element
        self._item = item


# Game


class GameEntry:
    _name: str
    _score: int

    def __init__(self, name: str, score: int) -> None:
        self._name = name
        self._score = score

    def __str__(self) -> str:
        return f"User's {self._name} score is {self._score}"

    def get_name(self) -> str:
        return self._name

    def get_score(self) -> int:
        return self._score


class Scoreboard:
    _entries_amount: int
    # Global state (shared between instances)
    _board: list[GameEntry]

    def __init__(self, capacity: int) -> None:
        self._board = []

    def __str__(self) -> str:
        return f"the current board is {self._board} with {len(self._board)} entries"


# play

entry_one = GameEntry("Carlos", 999)
print(f"entry one {entry_one}")

scoreboard = Scoreboard(5)
print(f"scoreboard {scoreboard}")
