arr = list(map(int,input("enter the elements of an array:").split()))
print("array:",arr)


def find_single_number(arr):
    xor = 0
    for i in range(len(arr)):
        xor = xor ^ arr[i]
    return xor

print("Number that appears once:", find_single_number(arr))