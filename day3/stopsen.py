sentences = ["a new world record was set","in the holy city of ayodha","on the eve of diwali on tuesday","with over three lakh diya or earthen lamps","lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for','a','of','the','and','to','in','on','with','was']
result = []
for i in sentences:
    resul1 = i.split()
    for j in resul1:
        if j in stopwords:
            continue
        else:
            result.append(j)    
print(result)

# using of 
for word in sentences:
    row = []
    for word in sentences.split():
        if word not in stopwords:
            row.append(word)
    result.append(word)    
print(result)

print([[word for word in sentences.split() if word not in stopwords]for senetence in sentences])
