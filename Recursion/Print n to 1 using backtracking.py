def printi(i,n):
    if i > n:
        return
    printi(i+1,n)
    print(i)

n= int(input("Enter the value of n:"))
printi(1,n)
# TC = O(N)
# SC = O(N)