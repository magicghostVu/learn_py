from typing import Generic, TypeVar, Optional
from oop.impl_linked_list.Node import Node
from oop.impl_linked_list.NodeUtils import NodeUtils

# biến type param (có thể sử dụng type bound)
T = TypeVar("T")


class LinkedList(Generic[T]):
    # tất cả các field nên được khởi tạo và khai báo kiểu ở constructor để IDE có thể gợi ý tốt nhất có thể
    def __init__(self) -> None:
        self.size: int = 0
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def add(self, e: T) -> None:
        # tăng size lên 1,
        self.size = self.size + 1
        if self.head is None:
            self.head = Node[T](e)
            self.tail = self.head
        else:
            new_node = Node[T](e)
            NodeUtils.set_next_for_node(self.tail, new_node)
            self.tail = new_node

    def get_first(self) -> Optional[T]:
        if self.head is None:
            return None
        # else:
        return self.head.data

    def get_tail(self) -> Optional[T]:
        if self.tail is None:
            return None
        else:
            return self.tail.data
