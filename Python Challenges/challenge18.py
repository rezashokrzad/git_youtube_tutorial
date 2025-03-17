#Sum of Digits: Write a program that calculates the sum of the digits of a number entered by the user.

def sOD(number):
    sum=0
    for i in number:
        sum += int(i)
    return sum
      
number=input("enter number: ")
print(sOD(number))

######### Solution 2 by Negar Deilami 3.15.25 
num = input('enter a number: ')
Sum = 0
for i in range(len(num)):
    Sum += int(num[i])
print(f"the sum of the digits of the number you entered is: {Sum}")