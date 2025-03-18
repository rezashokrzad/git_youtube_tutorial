# Problem: FizzBuzz: Print numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".
# Solution:
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#new solution:

def res(i):
    if i %15==0:
        return f"{i} : FizzBuzz"
    elif i%3==0:
        return f"{i} : Fizz"
    elif i%5==0:
        return f"{i} : Buzz"
    else:
        return i
    
    
for i in range(1,101):
    print(res(i))
