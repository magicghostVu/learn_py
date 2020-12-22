from oop.impl_linked_list.Node import Node
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


# hiển thị cũng rất ok
class NodeUtils(Generic[T]):
    @classmethod
    def set_next_for_node(cls, current_node: Optional[Node[T]], _next: Node[T]) -> None:
        if not current_node is None:
            current_node.__set_next__(_next)

    @classmethod
    def is_nex_none(cls, node: Node[T]) -> bool:
        return node.next is None
