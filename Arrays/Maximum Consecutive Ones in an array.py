arr = list(map(int,input("enter the elements of an array:").split()))
print("array:",arr)

def maximum(arr):
    i = 0 
    maxi = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] ==1:
            count +=1
            if count > maxi:
                maxi = count
        else:
            count = 0
    return maxi

print("Maximum consecutive ones in an array is :", maximum(arr))