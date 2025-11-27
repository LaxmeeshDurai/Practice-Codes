arr1 = list(map(int,input("enter the elements of first array:").split()))
arr2 = list(map(int,input("enter the elements of second array:").split()))

def intersection(arr1,arr2):
    interarr =[]
    i,j =0,0
    while i <len(arr1) and j <len(arr2):
        if arr1[i] == arr2[j]:
            interarr.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] > arr2[j]:
            j+=1
        else:
            i+=1

    return interarr

print("Intersection of two arrays:", intersection(arr1,arr2))