arr = list(map(int,input("enyter the elements of an array:").split()))
print("array:",arr)
k =int(input("enter the sum:"))

def longest_subarray_with_sum_k(arr,k):
    prefix_sum_map ={}
    max_length = 0
    current_sum = 0
    for i in range(0,len(arr)):
        current_sum += arr[i]
        if current_sum ==k:
            max_length+=1
        if (current_sum -k) in prefix_sum_map:
            max_length = max(max_length,i-prefix_sum_map[current_sum - k])

        if current_sum not in prefix_sum_map:
            prefix_sum_map[current_sum] = i
    return max_length

print("Longest subarray", longest_subarray_with_sum_k(arr,k))