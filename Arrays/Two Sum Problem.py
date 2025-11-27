nums = list(map(int,input("Enter the elements of an array:").split()))
print("Array:",nums)
target = int(input("Enter the target sum: "))
def two_sum(nums, target):
    num_map = {}
    for i, number in enumerate(nums):
        complement = target - number
        if complement in num_map:
            return [num_map[complement], i]
        num_map[number] = i
    return []

print("Indices of the two numbers that add up to target:", two_sum(nums, target))