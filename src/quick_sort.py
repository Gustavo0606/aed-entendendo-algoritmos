from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    def quicksort(array, min, max):
        if min >= max:
            return
        n_pivo = min
        pivo = array[max]
        for i in range(min, max):
            if array[i] < pivo:
                array[n_pivo], array[i] = array[i], array[n_pivo]
                n_pivo +=1
        array[n_pivo], array[max] = array[max], array[n_pivo]
        quicksort(array, min, n_pivo-1)
        quicksort(array, n_pivo+1, max)
        return array
    
    
    if len(array) == 1:
        return array
    elif not len(array):
        return array
    return quicksort(array, 0, len(array)-1)
    