def largest(arr):
    large = arr[0]
    for i in  range(0,len(arr)-1):
        if  arr[i] > large:
            large = arr[i]

    return large

arr = list(map(int,input("enter the elemnets of an array:").split()))
print("Largest number in an array is ",largest(arr))