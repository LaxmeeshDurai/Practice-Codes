arr = list(map(int,input("enter the elements of an array:").split()))
print("array",arr)

def majority1(arr):
    n = len(arr)
    c = 0
    for i in range(0,n):
        if c == 0:
            c = 1
            element = arr[i]
        elif element == arr[i]:
            c += 1
        else:
            c -= 1
    count = sum(1 for x in arr if x == element)
    if count > n//2 :
        return element
    else:
        return -1
    
print("element :",majority1(arr))