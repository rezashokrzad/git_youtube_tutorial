# Decimal to Binary Conversion: Write a program that converts a decimal number to binary.

######## Solution by Negar Deilami 3.15.25 
decimalNumber = int(input("give me a number to convert it to Binary: "))
binary = ''
if decimalNumber == 0:
    binary = '0'
else:
    while decimalNumber > 0:
        remainder = decimalNumber % 2
        binary = str(remainder) + binary
        decimalNumber = decimalNumber // 2

print("Binary:", binary)