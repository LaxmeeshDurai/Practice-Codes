def fact(i,factorial):
    if i < 1:
        print(factorial)
        return
    fact(i-1,factorial*i)

n = int(input("enter the value of n: "))
fact(n,1)