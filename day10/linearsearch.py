def linearsearch(arr,n,x):
    for i in range(0,n):
        if arr[i] == x:
            return i
    return -1    

arr = [2,4,0,1,9]    
n = len(arr)
x = 1
result = linearsearch(arr,n,x)
if result == -1:
    print("the element is not present in the array")
else:
    print("the element is found at index: ",result)    