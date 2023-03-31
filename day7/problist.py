l1 = ['A','app','a','d','ke','th','doc','awa']
l2 = ['y','tor','e','eps','ay',None,'le','n']
l2.reverse()
s =""
for i in range(len(l1)):
    if l1[i] == None or l2[i] == None:
        if l1[i] != None:
            s = s + l1[i] + " "

        else:
            s = s + l2[i]    
    else:
        s = s + l1[i] + l2[i] + " " 
print(s)

    

    
