from random import randint


def insertion_sort(array):
    """
    Sorts an array of integers in ascending order using the insertion sort algorithm.

    Args:
        array (list): A list of integers to be sorted.

    Returns:
        list: The sorted list of integers.
    """
    for _ in range(1,len(array)):
        actual_value = array[_]
        pos = _ - 1
        #we just shift one by one until array[pos] <= actual_value
        while pos >= 0 and array[pos] > actual_value:
            array[pos+1] = array[pos]
            pos -= 1

        array[pos+1] = actual_value

    return array


array = []
for _ in range(20):
    array.append(randint(0,30))

print(insertion_sort(array))