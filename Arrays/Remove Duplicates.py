def RemoveDuplicates(arr):
    if len(arr) == 0:
        return 0
    i = 0
    for j in range(i,len(arr)):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i+= 1
    return i + 1

arr = list(map(int,input("enter the elemnets of an array:").split()))
print("Length of array after removing duplicates is ",RemoveDuplicates(arr))
print("Array after removing duplicates is ",arr[:RemoveDuplicates(arr)])