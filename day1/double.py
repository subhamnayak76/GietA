no = int(input())
double = no*2;
num = str(no)
num2 = str(double)
flag = "true"
if len(num) == len(num2):
    for i in num:
        if  i in num2:
            continue
        else:
            flag = "false"
else:
    flag = "false"                


print(flag)
    

