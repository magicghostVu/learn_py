from typing import TypeVar, Generic

E = TypeVar('E')


class Node(Generic[E]):
    def __init__(self, data: E) -> None:
        self.data = data
        self.next: object = None

    def __set_next__(self, _next: object):
        self.next = _next
