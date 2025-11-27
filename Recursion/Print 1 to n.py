def printi(n, i):
    if i > n:
        return
    print(i)
    printi(n, i + 1)

n = int(input("enter the value of n: "))
printi(n, 1)
# TC = O(N)
# SC = O(N)