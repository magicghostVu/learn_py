from typing import Optional

from oop.impl_linked_list.MLinkedList import LinkedList

ll: LinkedList[int] = LinkedList[int]()
ll.add(5)
ll.add(8)

f: Optional[int] = ll.get_first()

print("f is", f)
print("size of list is", ll.get_size())
