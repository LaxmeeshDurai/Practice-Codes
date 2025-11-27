def permute(arr,start,end):
    if start == end:
        print(arr)
    else:
        for i in range(start,end +1):
            arr[start],arr[i] = arr[i],arr[start]
            permute(arr,start+1,end)
            arr[start],arr[i] = arr[i], arr[start]

arr= list(map(int,input("enter the elements of an array:").split()))
permute(arr,0,len(arr)-1)