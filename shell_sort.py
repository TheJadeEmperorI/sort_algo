from random import randint


def gapInsertionSort(array, start, gap):
    #for each index, at the gap chose.
    for index in range(start+gap, len(array), gap):
        actual_value = array[index]
        pos = index

        while pos >= gap and array[pos-gap] > actual_value:
            array[pos] = array[pos-gap]
            pos -= gap
        
        array[pos] = actual_value


def shell_sort(array):
    sublistcount = len(array)//2
    while sublistcount > 0:
        for startpos in range(sublistcount):
            gapInsertionSort(array, startpos, sublistcount)
        sublistcount = sublistcount//2

    return array


array = []
for _ in range(20):
    array.append(randint(0,30))

print(shell_sort(array))