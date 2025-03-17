# Factorial: Write a program that calculates the factorial of a number entered by the user.
num = int(input("Enter Your Number for calculates the factorial : "))
fact = 1
for i in range(1, num+1):
    fact*=i
print(f"Your Factorial: {fact}")

#new_solution:
number=int(input("enter a number: "))
factorial=1
if number<0:
    print(f"num is {number},factorial does not exist for negative numbers!")
elif number ==0:
    print(f"factorial of {number} is 1")
else:
    for i in range(1,number+1):
        factorial*=i
    print(f"the factorial of {number} is {factorial}")

######### Solution 3 by Negar Deilami 3.12.25 
number3 = int(input('give me an integer '))
num3 = 1
for i in range(1,number3+1):
    num3 = num3 * i
print(num3)
