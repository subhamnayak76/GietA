score = (12,18,25,24,2,5,18,20,20,21)
avg = []
avg = list(score)
result = sum(avg)/len(avg)
c = 0
for i in avg:
    if i >= result:
        c = c+1  
print(c*10)    
list1 =[]
# genterte frequncy
for  i in range(0,26):
    c = 0
    for j in range(0,len(avg)-1):
        if i == avg[j]:
            c = c+1
    list1.append(c)        
            
    

print(list1)