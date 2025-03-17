# Linear Search: Write a program that implements linear search.

######### Solution by Negar Deilami 3.16.25
def linearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            print(f"your desired value is at index {i}")
            return
    print('Not Found')
    
linearSearch([2,5,7,1,9,8,10,3,23,45], 4) # test