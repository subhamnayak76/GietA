st = "infosys 12"  
n = 0
c = 0
for i in st:
    if i.isdigit():
        n = n+1
    elif i.isalpha():
        c = c+1
    else:
        continue
list = [n,c]
print(list)