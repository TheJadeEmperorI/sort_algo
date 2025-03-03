from random import randint

#this verion is not optimized
def bubble_sort(array):
    """
    Sorts an array of integers in ascending order using the bubble sort algorithm.

    Args:
        array (list): A list of integers to be sorted.

    Returns:
        list: The sorted list of integers.
    """
    for passnum in range(len(array)-1,0,-1):
        for i in range(_):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    
    return array


def bubble_sort_optimized(array):
    """
    Sorts an array of integers in ascending order using the bubble sort algorithm.

    Args:
        array (list): A list of integers to be sorted.

    Returns:
        list: The sorted list of integers.

    NB : Here if we didn't do a single swap, it means the array is already sorted.
    """
    exchange = True
    passnum = len(array)-1

    while exchange and passnum > 0:
        exchange = False
        for i in range(passnum):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                exchange = True

        passnum -= 1

    return array


array = []
for _ in range(10000):
    array.append(randint(0,10000))

print(bubble_sort_optimized(array))