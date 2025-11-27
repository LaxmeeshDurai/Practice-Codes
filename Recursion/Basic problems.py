def printName(n,i):
    if i > n:
        return
    print("Raja")
    printName(n, i+1)

n = int(input("enter the value of n:"))
printName(n, 1)
# TC = O(N) 
# SC = O(N)
