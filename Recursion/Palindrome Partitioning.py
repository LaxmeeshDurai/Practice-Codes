def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def partition_helper(s: str, start: int, path: list, result: list):

    if start == len(s):
        result.append(path[:])  # add a copy of the path
        return

    for end in range(start + 1, len(s) + 1):
        substring = s[start:end]
        if is_palindrome(substring):
            # Choose
            path.append(substring)
            # Explore further
            partition_helper(s, end, path, result)
            # Backtrack
            path.pop()

def palindrome_partitioning(s: str):
    result = []
    partition_helper(s, 0, [], result)
    return result


s = "aabb"
print("All palindrome partitions of", s, "are:")
print(palindrome_partitioning(s))
