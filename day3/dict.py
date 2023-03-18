mylist = [9,3,6,1,5,0,8,2,4,7]
listb = [6,4,6,1,2,2]
dic = {}
for i in listb:
    dic[i] = mylist.index(i)
print(dic)

#using list compherension
print( {i: mylist.index(i) for i in listb})