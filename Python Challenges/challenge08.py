# Bubble Sort: Write a program that implements bubble sort.

######### Solution by Negar Deilami 3.13.25 
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
             array[j], array[j + 1] = array[j + 1], array[j]
    print(array)

# example 
bubbleSort([7, 8, 5, 1, 4, 3, 7, 13])