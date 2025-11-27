arr1 = list(map(int,input("enter the elements of array 1: ").split()))
arr2 = list(map(int,input("enter the elements of array 2: ").split()))

def union(arr1, arr2):
    i,j =0,0
    Union = []
    while i < len(arr1) and j <len(arr2):
        while i > 0 and i < len(arr1) and arr1[i] == arr1[i-1]:
            i+=1
        while j > 0 and j < len(arr2) and arr2[j] == arr2[j-1]:
            j+=1
        if i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                Union.append(arr1[i])
                i+=1
            elif arr1[i] > arr2[j]:
                Union.append(arr2[j])
                j+=1
            else:
                Union.append(arr1[i])
                i+=1
                j+=1
    while i < len(arr1):
        if i == 0 or arr1[i] != arr1[i-1]:
            i+=1
    while j < len(arr2):
        if j == 0 or arr1[j] != arr1[j-1]:
            Union.append(arr2[j])
            j+=1

    return Union

print("Union of two arrays:", union(arr1,arr2))