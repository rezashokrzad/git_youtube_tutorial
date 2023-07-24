#GCD and LCM: Write a program that calculates the greatest common divisor (GCD) and least common multiple (LCM) of two numbers entered by the user.

def GCD(num1,num2):
    if num1>num2:
        F_GCD=num1
    else:
        F_GCD=num2
    while True:
        if (num1%F_GCD == 0) and (num2 % F_GCD==0):
            break
        F_GCD -=1
    return F_GCD

def LCM(num1,num2):
    return (num1*num2) // GCD(num1,num2)
        
number1=int(input("ٍenter the first number: "))
number2=int(input("enter the second number:  "))
print("GCD is: ",GCD(number1,number2))
print("LCM is : ",LCM(number1,number2))
