# Factorial: Write a program that calculates the factorial of a number entered by the user.
num = int(input("Enter Your Number for calculates the factorial : "))
fact = 1
for i in range(1, num+1):
    fact*=i
print(f"Your Factorial: {fact}")

# or 
# num = int(input("Enter Your Number for calculates the factorial : "))
# fact = 1
# for i in range(1, num+1):
    # fact *= i
    # print(f"Step {i} → next: {fact}", end=", ")
