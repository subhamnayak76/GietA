arr = [1,2,3,4,5,6,7,8,9,10]
x = 7
start = 0
res = -1
end = len(arr) - 1
while start <= end:
    mid = (start +end)//2
    
    if arr[mid] == x:
        res = mid
        break
    elif arr[mid] < x:
        start = mid + 1
    else:
        end = mid - 1
if res == -1:
    print("the element is not found")
else:
    print("element is present at index",res)    

