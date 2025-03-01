from random import randint


def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0 #index for the left part
        j = 0 #index for the right part
        k = 0 #index for the array

        #here we just put one by one the smaller
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k = k+1
        
        #we put the remain, we don't have to check because it's already sorted.
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


array = []
for _ in range(20):
    array.append(randint(0,30))

print(merge_sort(array))