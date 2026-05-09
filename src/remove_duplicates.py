from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    cabeca = head
    while cabeca:
        proximo = cabeca
        while proximo.next:
            if cabeca.value == proximo.next.value:
                proximo.next = proximo.next.next
            else:
                proximo = proximo.next
        cabeca = cabeca.next
    return head
