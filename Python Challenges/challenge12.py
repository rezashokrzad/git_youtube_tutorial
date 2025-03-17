#Find the Largest Element: Write a program that finds the largest element in an array.

#1:
numbers=[9865,156,3,59856,15,65,48,156987,99]
numbers.sort()
print(numbers[-1])

#2:
print(max(numbers))
 
######### Solution 2 by Negar Deilami 3.8.25 
array = list(input('give me a list of Elements seperated by comma: ').split(","))
array.sort(reverse=True)
print('the Largest Element is',array[0])