# Selection Sort: Write a program that implements selection sort.

######### Solution by Negar Deilami 3.17.25
array = [2,3,5,6,1,9]
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
                if array[j] < array[min_index]:
                 min_index = j
    array[i], array[min_index] = array[min_index], array[i] #swap the two

print(array)