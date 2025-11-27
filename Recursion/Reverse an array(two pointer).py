def reverse(a , left , right):
    if (left >= right):
        return
    a[left], a[right] = a[right], a[left]
    reverse(a , left+1 , right-1)

arr = list(map(int,input("Enter the elements of an array:").split()))
reverse(arr , 0 , len(arr)-1)
print("Reversed array:", arr)