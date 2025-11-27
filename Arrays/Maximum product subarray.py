arr = list(map(int,input("enter the elements of an array:").split()))
print("array:",arr)

def max_product_subarray(arr):
    prefix = 1
    suffix = 1
    result = float('-inf')
    n = len(arr)
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix *= arr[i]
        suffix *= arr[n-i-1]
        result = max(result,prefix,suffix)
    return result

print("Maximum product subarray is :", max_product_subarray(arr))