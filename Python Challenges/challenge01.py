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


# Object-oriented solution:
class FizzBuzz:
    def __init__(self, start: int = 1, end: int = 100):
        self.start = start
        self.end = end

    def check(self, number: int) -> str:
        if number % 15 == 0:
            return f"{number} : FizzBuzz"
        elif number % 3 == 0:
            return f"{number} : Fizz"
        elif number % 5 == 0:
            return f"{number} : Buzz"
        else:
            return str(number)

    def run(self):
        for i in range(self.start, self.end + 1):
            print(self.check(i))


# Instantiate and run the FizzBuzz logic
if __name__ == "__main__":
    fb = FizzBuzz()
    fb.run()

