from random import randint

def selection_sort(array):
    """
    Sorts an array of integers in ascending order using the selection sort algorithm.

    Args:
        array (list): A list of integers to be sorted.

    Returns:
        list: The sorted list of integers.
    """
    for _ in range(len(array)-1,0,-1):
        maxi = _
        for i in range(_):
            if array[i] > array[maxi]:
                maxi = i
        
        array[maxi], array[_] = array[_], array[maxi]
    
    return array

array = []
for _ in range(20):
    array.append(randint(0,30))

print(selection_sort(array))