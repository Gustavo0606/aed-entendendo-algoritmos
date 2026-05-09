from src.my_array import MyArray


def two_sum(array: MyArray, target: int) -> tuple[int, int]:
    for i in range(len(array)):
        valorUM = array[i]
        for a in range(i+1, len(array)):
            valorDois = array[a]
            if valorUM + valorDois == target:
                return (i, a)
    return (-1, -1)
