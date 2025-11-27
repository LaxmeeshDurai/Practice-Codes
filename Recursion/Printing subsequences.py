def sub(index,current):
    if index >= n:
        print(current)
        return
    current.append(arr[index])
    sub(index+1, current)
    current.pop()
    sub(index+1,current)

arr = list(map(int,input("enter the elements of an array:").split()))
n= len(arr)
sub(0,[])