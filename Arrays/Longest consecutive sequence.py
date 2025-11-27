arr = list(map(int,input("enter the elements of an array:").split()))
print("array:",arr)

def longest_consecutive_sequence(arr):
    n = len(arr)
    if n==0:
        return False
    Longest = 1
    set_arr = set(arr)
    for num in set_arr:
        if num - 1 not in set_arr:
            current_num = num
            current_streak = 1
            while current_num + 1 in set_arr:
                current_num += 1
                current_streak += 1
            Longest = max(Longest, current_streak)
    return Longest

result = longest_consecutive_sequence(arr)
print("Length of the longest consecutive sequence is:", result)