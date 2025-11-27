arr = list(map(int,input("enter the elements of an array:").split()))
k = int(input("enter the sum:"))

def count_subarrays_sum_k(arr, k):
    left = 0
    curr_sum = 0
    count = 0

    for right in range(len(arr)):
        curr_sum += arr[right]

        # shrink window while sum > k
        while curr_sum > k and left <= right:
            curr_sum -= arr[left]
            left += 1

        # if exact match
        if curr_sum == k:
            count += 1

    return count


print("Count of subarrays with sum", k, "is:", count_subarrays_sum_k(arr, k))
