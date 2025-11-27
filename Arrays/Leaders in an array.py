arr = list(map(int,input("enter the elemnets of an array:").split()))
print("array:",arr)

def leader(arr):
    maxi = 0
    n = len(arr)
    result= []
    for i in range(n-1,-1,-1):
        if arr[i] > maxi:
            maxi = arr[i]
            result.append(maxi)
    return result

print("the leaders in an array is :", leader(arr))