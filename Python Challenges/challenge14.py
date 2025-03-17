#Count the Number of Characters: Write a program that counts the number of characters in a string.
def Count(text):
    result=len([i for i in text if i.isalpha()])
    return result
string=input("enter string : ")
print(Count(string))


######### Solution 2 by Negar Deilami 3.13.25
string1 = input('give me a string, I will count the number of characters: ')
count =0
for i in string1 :
    count += 1
print(f"your string is composed of \033[1m{count}\033[0m characters")