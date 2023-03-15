#count the no of subarray with  distinct the sum of  subarray with odd integer
start = int(input())
end = int(input())
list1=[]
for i in range(start,end+1):
    list1.append(i)

# list comprehension 
array = [i for i in range(start,end+1)]    
c  = 0  
list2 = []
for i in range(len(list1)):
    sum  = 0
    for j in range(i,len(list1)):
        list2.append(list1[i:j+1])

        # sum += list1[j]
            # if sum % 2 != 0:
            #     c = c+1
print(list2)

#checking for odd sum
n = len(list1)
for i in range(n):
    sum = 0
    for j in range(i,n):
       sum += list1[j]
       if sum % 2 != 0:
           c =c+1 
print(c)           