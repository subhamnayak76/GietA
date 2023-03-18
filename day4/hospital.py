dic = {"P": "Pediatrics","O":"Orthopedics","E": "ENT"}
list1 = [101,'P',102,'O',302,'P',305,'P']
nop = "P"
noo = "O"
noe = "E"
c = 0
c1 = 0
c2 = 0
for i in list1:
    if i == nop:
        c = c+1
    elif i == noo:
        c1 = c1+1
    elif i == noe:
        c2 = c2+1
res = max(max(c,c1),c2)
s = ""
if res == c:
    s = dic['P']
elif res == c1:
    s = dic['O']
else:
    s = dic['E']    
print(s)           
# for i in  dic:
# res = " "
# res = dic['s']    
# print(res)
# list count function list.count("P")
