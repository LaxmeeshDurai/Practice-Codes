def reverse(a, i):
    n = len(a)
    if i >= n // 2:   
        return

    a[i], a[n - i - 1] = a[n - i - 1], a[i]
    reverse(a, i + 1)

arr = list(map(int, input("Enter the elements of an array: ").split()))
reverse(arr, 0)

print("Reversed array:", arr)
