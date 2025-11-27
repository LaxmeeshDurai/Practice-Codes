arr = list(map(int,input("enter the elements of an array:").split()))
print("array:",arr)

def three_sum(a):
    n = len(a)
    a.sort()
    result = []
    for i in range(n-2):
        if i > 0 and a[i] == a[i-1]:
            continue
        l = i+1
        r = n-1
        while l < r:
            total = a[i] +a[l] + a[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                triplet = [a[i], a[l], a[r]]
                result.append(triplet)
                while l < r and a[l] == triplet[1]:
                    l += 1
                while l < r and a[r] == triplet[2]:
                    r -= 1
                l += 1
                r -= 1
    
    return result

print("Triplets with sum zero are:", three_sum(arr))