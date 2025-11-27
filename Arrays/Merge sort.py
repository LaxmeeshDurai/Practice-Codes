arr = list(map(int,input("enter the elements of an array:").split()))
print("array:",arr)
n= len(arr)

def merge_sort(arr,l,r):
    if l >= r:
        return
    m = (l+r)//2
    merge_sort(arr,l,m)
    merge_sort(arr,m+1,r)
    merge(arr,l,m,r)

def merge(arr,l,m,r):
    temp =[]
    i = l
    j = m+1
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= m:
        temp.append(arr[i])
        i += 1
    while j <= r:
        temp.append(arr[j])
        j += 1
    for k in range(l,r+1):
        arr[k] = temp[k-l]

merge_sort(arr,0,n-1)
print("Sorted array using merge sort is :", arr)