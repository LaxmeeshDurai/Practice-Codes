def printi(i,n):
    if i< 1:
        return
    printi(i-1,n)
    print(i)

n= int(input("Enter the value of n:"))
printi(n,n)
# TC = O(N)
# SC = O(N)