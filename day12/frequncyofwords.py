text = "good bad good"
l = []
for i in text.split():
    l.append(i)
dic = {}
for i in l:
    if  i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
res = -1
for value in dic.values():
    res = max(res,value)
postiton = dic.index(res)
print(dic[postiton])       

