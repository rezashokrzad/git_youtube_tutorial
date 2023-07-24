#Sum of Digits: Write a program that calculates the sum of the digits of a number entered by the user.

def sOD(number):
    sum=0
    for i in number:
        sum += int(i)
    return sum
      
number=input("enter number: ")
print(sOD(number))
