#Count the Number of Characters: Write a program that counts the number of characters in a string.
def Count(text):
    result=len([i for i in text if i.isalpha()])
    return result
string=input("enter string : ")
print(Count(string))
