def slargest(arr):
    large = arr[0]
    slarge = -1
    for i in  range(0,len(arr)-1):
        if  arr[i] > large:
            slarge = large
            large = arr[i]
        if arr[i] > slarge and arr[i] > large:
            slarge = arr[i]

    return slarge

arr = list(map(int,input("enter the elemnets of an array:").split()))
print("Second Largest number in an array is ",slargest(arr))