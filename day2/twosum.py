list1= [1,2,7,4,5,6,0,3]
k = 6
c =0
n = len(list1)
for i in range(0,n):
    for j in range(i+1,n-1):
        if list1[i] + list1[j] == k:
            c = c+1
print(c)


# list1.sort()
# k = 6
# i = 0
# j = len(list1)-1

# c = 0
# while  i < j:
#     if list1[i] + list1[j] == k:
#         c = c + 1
#     i = i + 1
#     j = j - 1
        
# print(c)


