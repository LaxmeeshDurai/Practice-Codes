arr = list(map(int,input("enter the elements of an array:").split()))
print("array:",arr)

def rearrange(arr):
    pos = 0
    neg = 1
    result = [0] * len(arr)
    for i in range(len(arr)):
        if arr[i] >= 0:
            result[pos] = arr[i]
            pos += 2
        elif arr[i] < 0:
            result[neg] = arr[i]
            neg += 2
    return result

print("Rearranged array based on sign is :", rearrange(arr))