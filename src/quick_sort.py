from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    def quick_sort(array):
        if len(array) <= 1:
            return array
        esquerda = MyArray()
        direita = MyArray()
        pivo = MyArray()
        pivo.append(array[0])
        for i in range(1, len(array)):
            if array[i] < pivo[0]:
                esquerda.append(array[i])
            else:
                direita.append(array[i])
        return merge(merge(quick_sort(esquerda), pivo), quick_sort(direita))

    def merge(array1, array2):
        novoArr = MyArray()
        contador1 = 0
        contador2 = 0
        while len(array1) > contador1 and len(array2) > contador2:
            if array1[contador1] < array2[contador2]:
                novoArr.append(array1[contador1])
                contador1 += 1
            else:
                novoArr.append(array2[contador2])
                contador2 += 1

        for i in range(contador1, len(array1)):
            novoArr.append(array1[i])
        for a in range(contador2, len(array2)):
            novoArr.append(array2[a])
        return novoArr
    return quick_sort(array)
