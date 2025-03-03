from random import randint

#VERSION1
def partition(array, g, d):
    pivot = array[d]
    i = g - 1
    for j in range(g,d):
        if array[j] <= pivot:
            #we just swap around the pivote
            i = i +1
            array[i], array[j] = array[j], array[i]
    
    #we put the pivot at the center
    array[i+1], array[d] = array[d], array[i+1]
    return i + 1


def quick_sort_version1(array, g, d):
    if g < d:
        p = partition(array, g, d)
        quick_sort_version1(array, g, p-1)
        quick_sort_version1(array, p+1, d)

    return array

#VERSION2 MY FAVORITE
def quick_sort_version2(array, g, d):
    if g < d:
        i = g
        j = d
        pivot = array[(i+j)//2]
        while True:
            while array[i] < pivot:
                i = i + 1
            while array[j] > pivot:
                j = j - 1
            if i >= j:
                break
            
            array[i], array[j] = array[j], array[i]
            i = i + 1
            j = j - 1
            
        quick_sort_version2(array, g, i -1)
        quick_sort_version2(array, j+1,d)

    return array

#VERSION3 (That's really ugly, in my opinion).
def partition_2(array, g, d):
    pivot = array[g]
    #we take the element after the pivot
    i = g + 1
    j = d

    done = False
    while not done:
        while i<=j and array[i] < pivot:
            i = i + 1
        
        while array[j] > pivot and j >= i:
            j = j - 1
        
        if j < i:
            done = True
        
        else:
            array[i], array[j] = array[j], array[i]
            i = i + 1
            j = j - 1
    array[g], array[j] = array[j], array[g]
    return j


def quick_sort_version3(array, g, d):
    if g < d:
        p = partition(array, g, d)
        quick_sort_version3(array, g, p-1)
        quick_sort_version3(array, p+1, d)

    return array

'''
NOTE : I'm gonna use the version 2 for the optimisations, I find this on the most elegant
'''
def quick_sort_optimised(array, g, d):
    '''
    In this optimisation, I only sort the shortest vector. 

    -> No need to worry about the pivot now, we won't sort the largest.
    '''

    #need to replace the if with a while, because we'll try again and again
    #with the shortest
    while g < d:
        i = g
        j = d
        mid = (i+j)//2
        pivot = array[mid]
        while True:
            while array[i] < pivot:
                i = i + 1
            while array[j] > pivot:
                j = j - 1
            if i >= j:
                break
            
            array[i], array[j] = array[j], array[i]
            i = i + 1
            j = j - 1
        
        #if the right part is smaller
        if (i-g) < (d-j):
            quick_sort_optimised(array, g, i -1)
            g += 1

        #if the left part is smaller
        else:
            quick_sort_optimised(array, j+1,d)
            d -= 1

    return array

'''
NOTE : quick sort Class optimisation 
'''
class QuickSort():
    
    def __init__(self, array):
        self.array = array
    

    def sort(self):
        self.quick_sort_optimised2(0,len(self.array)-1)
        print(self.array)


    def quick_sort_optimised2(self, g, d):
        while g < d:
            i = g
            j = d
            mid = (i+j)//2
            pivot = self.array[mid]
            while True:
                while self.array[i] < pivot:
                    i = i + 1
                while self.array[j] > pivot:
                    j = j - 1
                if i >= j:
                    break
                
                self.array[i], self.array[j] = self.array[j], self.array[i]
                i = i + 1
                j = j - 1
            
            if (i-g) < (d-j):
                self.quick_sort_optimised2(g, i -1)
                g += 1

            else:
                self.quick_sort_optimised2(j+1,d)
                d -= 1


array = []
for _ in range(20):
    array.append(randint(0,30))

a = QuickSort(array)
a.sort()