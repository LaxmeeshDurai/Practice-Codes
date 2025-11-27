def printi(n, i):
    if i < 1:
        return
    print(i)
    printi(n, i - 1)

n = int(input("enter the value of n: "))
printi(n, n)
# TC = O(N)
# SC = O(N)