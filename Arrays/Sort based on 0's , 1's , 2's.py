arr = list(map(int,input("enter the elements of an array:").split()))
print("array:",arr)
n = len(arr)
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def sort_0s_1s_2s(arr, n):
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if arr[mid] == 0:
            swap(arr, low, mid)
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            swap(arr, mid, high)
            high -= 1
    return arr

print("Sorted array:", sort_0s_1s_2s(arr, n))