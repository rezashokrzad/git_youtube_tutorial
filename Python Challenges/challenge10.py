# Quick Sort: Write a program that implements quick sort.

######### Solution by Negar Deilami 3.16.25
def quickSort(array):
    if len(array) <= 1:
     return(array)
    right = []
    left = []
    pivot = array[-1]
    for i in array[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
            
    return quickSort(left) + [pivot] + quickSort(right)

print(quickSort([1,4,7,9,3,6]))
