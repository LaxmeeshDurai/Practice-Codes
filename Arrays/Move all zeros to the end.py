arr = list(map(int,input("enter the elemnets of an array:").split()))
print("Original array:", arr)

def move_zeroes_to_end(arr):
    n = len(arr)
    j= 0
    for i in range(0,n):
        if arr[i] != 0:
            arr[j] = arr[i]
            j +=1

    for i in range(j,n):
        arr[i] = 0
    
    return arr

print("array after moving zeroes to the end :", move_zeroes_to_end(arr))