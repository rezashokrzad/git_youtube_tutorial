Reverse String: Write a program that takes a string as input and outputs the string reversed.

def reverse_string(input_string):
  reversed_str = input_string[::-1]
  return reversed_str

# Calling function
user_input = input("Enter a favorite string: ")
reversed_input = reverse_string(user_input)
print("Reversed string:", reversed_input)
