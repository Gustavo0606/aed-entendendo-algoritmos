from src.my_node import MyNode


def reverse_linked_list(head: MyNode) -> MyNode:
    anterior = None
    atual = head
    length = 0
    while atual is not None:
        proximo = atual.next
        atual.next = anterior
        anterior = atual
        atual = proximo
        length += 1
    if length == 0:
        return None
    return anterior
