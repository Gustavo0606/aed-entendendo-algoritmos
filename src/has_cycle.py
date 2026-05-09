from src.my_node import MyNode


def has_cycle(head: MyNode) -> bool:
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while fast is not None and fast != slow:
        if fast.next is None or fast.next.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True
