def nCr(r,c):
    ans = 1
    for i in range(c):
        ans = ans*(r-i)
        ans = ans//(i+1)
    return ans

row = int(input("Enter the number of rows for Pascal's Triangle: "))

for i in range(row):
    print(' '*(row-i), end='')
    for j in range(i+1):
        print(nCr(i,j), end=' ')
    print()