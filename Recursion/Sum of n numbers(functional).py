def sum2(n):
    if n==0:
        return 0
    return n + sum2(n-1)

n = int(input("Enter the value of n: "))
print(sum2(n))
