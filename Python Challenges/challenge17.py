#  Armstrong Number: Write a program that checks whether a given number is an Armstrong number or not.

######### Solution by Negar Deilami 3.16.25
number = input('insert a Number: \n')
exponent = len(number)
sum = 0
for i in number:
    sum += int(i)**exponent
if sum == int(number):
    print('Hooray! the given number is an Armstrong Number!')
else:
    print('your number is not an Armstrong Number.')
    
# test 153, 370 and 9494 as Armstrong Numbers 
# (1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153) 
# (9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474)