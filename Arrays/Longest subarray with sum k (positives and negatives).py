arr = list(map(int,input("enter the elements of an array:").split()))
print("array:",arr)
k = int(input("enter the sum:"))

def longest_subarray_sum_k(arr, k):
    prefix_sum = 0
    max_len = 0
    mp = {}   # stores: prefix_sum : earliest_index

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # Case 1: subarray from 0 to i has sum = k
        if prefix_sum == k:
            max_len = max(max_len, i + 1)

        # Case 2: subarray from some index+1 to i has sum = k
        if (prefix_sum - k) in mp:
            max_len = max(max_len, i - mp[prefix_sum - k])

        # Store prefix sum if first occurrence
        if prefix_sum not in mp:
            mp[prefix_sum] = i

    return max_len

print("Length of longest subarray with sum", k, "is:", longest_subarray_sum_k(arr, k))