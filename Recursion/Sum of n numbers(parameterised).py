def sum1(i,sum):
    if i < 1:
        print(sum)
        return
    sum1(i-1,sum+i)

n = int(input("enter the value of n: "))
sum1(n,0)