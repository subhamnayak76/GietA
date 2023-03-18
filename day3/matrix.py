mat =[[1,2,3,4] ,[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result =[]
for i in mat:
    for j in i:
        if   j % 2 == 0:
            result.append(j**3)
        else:
            result.append(j**2)    
print(result) 

print([j**3 if j % 2 == 0 else j**2 for i in mat for j in i])

resut = [] 
for i in mat:
    two = []
    for j in i:
        if j % 2 == 0:
            two.append(j**3)
        else:
            two.append(j**2) 
    resut.append(two)
print(resut)   
#list compherensio
print([[j**3 if j % 2 == 0 else j**2 for j in i]for i in mat])