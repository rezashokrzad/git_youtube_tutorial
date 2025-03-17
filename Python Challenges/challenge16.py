#Prime Numbers: Write a program that determines whether a given number is prime or not.

# def isprime(num):
#     acc=0
#     for i in range(1,num+1):
#         if num%i==0:
#             acc+=1
#     return True if acc==2 else False

# num=int(input("enter a number: "))
# print(isprime(num))
    

######### Solution 2 by Negar Deilami 3.13.25

theNum = int(input("insert a number to test its primality: "))
prime = 1
for i in range(theNum-2):
    if theNum % (i+2) == 0:
        prime = 0
if prime:
    print("the given number is Prime")
else:
    print("the given number is NOT Prime")
    