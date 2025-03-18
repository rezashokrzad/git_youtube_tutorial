#Count the Number of Words: Write a program that counts the number of words in a string.
def count_words(string):
    # Remove leading and trailing whitespace
    string = string.strip()
    # Split the string into words
    words = string.split()
    # Return the count of words
    return len(words)

# User interface & Test the function
print("Word Count Program")
print("------------------")
while True:
    input_string = input("Enter a string (or 'q' to quit): ")
    if input_string.lower() == 'q':
        break
    word_count = count_words(input_string)
    print("The number of words in the string is:", word_count)
    print()

print("Thank you for using the Word Count Program. Goodbye!")


#new_solution:
def CountOfWord(text):
    return len([i for i in text.split() if i.isalpha()])
text=input("enter string: ")
print(CountOfWord(text))


