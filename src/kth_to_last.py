from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    length = 0
    termo_contagem = head
    while termo_contagem:
        length += 1
        termo_contagem = termo_contagem.next
    if k > length or k <= 0:
        return -1
    if length == 0:
        return None
    termo = head
    indice = length - k
    busca = 0
    while indice > busca:
        termo = termo.next
        busca += 1
    return termo.value
