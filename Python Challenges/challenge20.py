# Binary to Decimal Conversion: Write a program that converts a binary number to decimal.

######### Solution by Negar Deilami 3.15.25 
BinaryNumber = input("insert a binary number:\n")
MaxExponent = len(BinaryNumber)-1
DecimalNumber = 0
for i in range(len(BinaryNumber)):
    DecimalNumber += (2**(MaxExponent-i))*int(BinaryNumber[i])
print(DecimalNumber)