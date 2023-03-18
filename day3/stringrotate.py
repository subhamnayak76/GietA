st = " rhdt:246,ghftd:1246"
se =[]
num = []
s = st.split(',')
for i in st:
    s1,n = i.split(":")
    se.append(s1)
    num.append(n)

def rotate(ss,n):
    sum = 0 
    for i in n:
        sum += int(i)**2
        if sum % 2 == 0:
            return se[-1] + s[:-1]
    else:
        return se[2]



for i in range(len(num)):
    print(se[i],num[i])

        
