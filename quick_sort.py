from random import randint


def partition(array, g, d):
    pivot = array[d]
    i = g - 1
    for j in range(g,d):
        if array[j] <= pivot:
            i = i +1
            array[i], array[j] = array[j], array[i]
        
    array[i+1], array[d] = array[d], array[i+1]
    return i + 1


def quick_sort(array, g, d):
    if g < d:
        p = partition(array, g, d)
        quick_sort(array, g, p-1)
        quick_sort(array, p+1, d)
    return array



array = []
for _ in range(20):
    array.append(randint(0,30))

print(quick_sort(array,0,len(array)-1))