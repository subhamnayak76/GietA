mylist = [9,3,6,1,5,0,8,2,4,7]
listb = [6,4,6,1,2,2]
new = []
for i in listb:
        new.append((i,mylist.index(i)))
print(new)    

#list compherension
print([(i,mylist.index(i)) for i in listb ])