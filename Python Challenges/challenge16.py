#Prime Numbers: Write a program that determines whether a given number is prime or not.

def isprime(num):
    acc=0
    for i in range(1,num+1):
        if num%i==0:
            acc+=1
    return True if acc==2 else False

num=int(input("enter a number: "))
print(isprime(num))
    
