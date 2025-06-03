# Palindrome: Write a program that checks whether a given string is a palindrome or not.

def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Example usage
text = input("Enter a string: ")
if is_palindrome(text):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
