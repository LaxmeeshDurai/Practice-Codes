n = int(input("Enter a decimal number: "))

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

print("Binary representation:", decimal_to_binary(n))

# TC = O(log n)
# SC = O(log n)