size = int(input("enter the size of the array:"))
array = list(map(int,input("enter the elements of an array:").split()))
n = int(input("enter the number of elements to be rotated :"))
n = n%len(array)


def reverse(subarray,start,end):
    while start < end:
        subarray[start],subarray[end] = subarray[end],subarray[start]
        start +=1
        end -=1

reverse(array,0,len(array)-1)
reverse(array,0,n-1)
reverse(array,n,len(array)-1)

print(f"the array after right rotated by {n} places :", array)