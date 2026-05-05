from src.my_array import MyArray


def reverse_array(array: MyArray) -> MyArray:
    esquerda = 0
    direita = len(array) -1
    while esquerda < direita:
        array[esquerda] , array [direita] = array [direita], array [esquerda]
        esquerda += 1
        direita -= 1
    return array
