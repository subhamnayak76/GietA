st = "3,2,6,5,1,4,8,9"
list1 =[]
for i in st.split(','):
    list1.append(int(i))
print(list1)
start = list1.index(5)
end = list1.index(8) 
sum = 0   
s = " "
for i in range(len(list1)):
    if  i < start :
        sum += list1[i]    
    elif i > end:
        sum += list1[i]    
print(sum)
s = ""
for i in range(start,end+1):
    s += str(list1[i])
print(s)
total = int(s)+sum
print(total)