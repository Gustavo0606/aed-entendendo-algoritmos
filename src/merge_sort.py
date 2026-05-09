from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    def mergesort(array):
        if len(array) <= 1:
            return array
        else:
            metade = len(array)//2
            esquerda = MyArray()
            direita = MyArray()
            for i in range(0, metade):
                esquerda.append(array[i])
            for a in range(metade, len(array)):
                direita.append(array[a])
            return merge(mergesort(esquerda), mergesort(direita))

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
    return mergesort(array)
