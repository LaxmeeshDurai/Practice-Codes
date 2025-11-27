arr = list(map(int,input("enter the lement of an array").split()))
print("array:",arr)
def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1
        return arr
    
def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

def permutation(a):
    n = len(a)
    index = -1
    for i in range(n-2,-1,-1):
        if a[i+1] > a[i]:
            index = i
            break
    if index == -1:
        reverse(a,0,n-1)
    for i in range(n-1,index,-1):
        if a[i] > a[index]:
            swap(a,i,index)
            break

    reverse(a,index+1,n-1)
    return a

print("Next PErmutation :",permutation(arr))