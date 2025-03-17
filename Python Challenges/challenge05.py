# Reverse String: Write a program that takes a string as input and outputs the string reversed.

def reverse_string(input_string):
  reversed_str = input_string[::-1]
  return reversed_str

# Calling function
user_input = input("Enter a favorite string: ")
reversed_input = reverse_string(user_input)
print("Reversed string:", reversed_input)


#new_solution;
def reverse(string):
    string="".join(reversed(string))
    print(f"reversed string is {string}",end="")

string=input("enter string:")
print(f"orginal string: {string}")
reverse(string)

######### Solution 3 by Negar Deilami 3.12.25
print()
theString = input('give me a String I will reverse it for you: ')
print(theString[::-1])