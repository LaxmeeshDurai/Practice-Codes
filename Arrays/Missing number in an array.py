arr = list(map(int,input("Enter the elements of an array:").split()))
print("Array:",arr)
N = len(arr) + 1
def missing_number(arr, N):
    xor1 = 0
    xor2 = 0
    for i in range(0,len(arr)):
        xor2 = xor2^arr[i]
    for i in range(1,N+1):
        xor1 = xor1^i
    return xor1^xor2

print("Missing number in the array is:", missing_number(arr, N))