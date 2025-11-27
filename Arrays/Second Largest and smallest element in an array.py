def slargest(arr):
    large = arr[0]
    slarge = float('-inf')
    for i in  range(0,len(arr)):
        if  arr[i] > large:
            slarge = large
            large = arr[i]
        elif arr[i] > slarge and arr[i] != large:
            slarge = arr[i]

    return slarge

arr = list(map(int,input("enter the elemnets of an array:").split()))
print("Second Largest number in an array is ",slargest(arr))

def ssmallest(arr):
    small = arr[0]
    ssmall = float('inf')
    for i in  range(0,len(arr)):
        if  arr[i] < small:
            ssmall = small
            small = arr[i]
        if arr[i] < ssmall and arr[i] != small:
            ssmall = arr[i]

    return ssmall

arr = list(map(int,input("enter the elemnets of an array:").split()))
print("Second Smallest number in an array is ",ssmallest(arr))

