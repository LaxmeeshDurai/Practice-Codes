binary = int(input("Enter a binary number: "))
def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

print("Decimal representation:", binary_to_decimal(str(binary)))