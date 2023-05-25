Palindrome: Write a program that checks whether a given string is a palindrome or not.

def is_palindrome(string):
    # Remove whitespace and convert string to lowercase
    string = string.lower().replace(" ", "")
    # Check if the string is equal to its reverse
    return string == string[::-1]

# Test the function
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
