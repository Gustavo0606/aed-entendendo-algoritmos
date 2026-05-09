from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:
    cabeca = None
    atual = None
    menor1 = lista1
    menor2 = lista2
    if lista1 is None and lista2 is None:
        return None
    if lista1 is None:
        return lista2
    if lista2 is None:
        return lista1
    if menor1.value < menor2.value:
        cabeca = menor1
        atual = menor1
        menor1 = menor1.next
    else:
        cabeca = menor2
        atual = menor2
        menor2 = menor2.next
    while menor1 and menor2:
        if menor1.value < menor2.value:
            atual.next = menor1
            atual = menor1
            menor1 = menor1.next
        else:
            atual.next = menor2
            atual = menor2
            menor2 = menor2.next
    if menor1:
        atual.next = menor1
    else:
        atual.next = menor2
    return cabeca
