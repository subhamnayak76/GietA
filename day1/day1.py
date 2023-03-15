for i in range(1,101):
    print(i)
# range(start,end,step)
for i in range(1,101):
    if i % 2 != 0:
        print(i)

for i in range(1,101):
    if i % 2 == 0:
       print(i) 
#print(*no of objects ,sep ='',end='\n')

#100 to 1
 for i in range(100,0,-1):
     print(i,end" ")
#100 to 1 odd
 for i in range(99,0,-2):
     print(i,end=" ")
# 100 to 1 even
 for i in range(100,0,-2):
    print(i,end="")

# break
 for i in range(1,101):
     if( i == 50):
         break
     else:
         print(i)


# continue
 for i in range(1,101):
     if( i == 50):
         continue
     else:
         print(i)
# pass
# null statement which does nothing
for i in range(1,101):
     if( i == 50):
         pass
     else:
         print(i)
         
# function 
def function():
    print("it is a function")

function()


#parameter
def function2(num,num2):
    print("num",num1,"num2",num2)
function2(10,20)

#return
def add(n,m):
    a = n + m
    return a
print(function3(100,200)
      
 # implict type cast
def function4(n,m):
     a = n + m
    return a
print(function4(100,20.0))

# string + float in function
def function5(n,m):
    a = float(n) + m
    return a
print(function5)
#postional arguments
#keyword argument
#based on argumets

#postional argument
def function19(a,b,c,d):
    print(a,b,c,d)
function(a,b,c)

#keyword argument
def function20(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function(num4 = 10,num2 = 6,num3 = 17,num1=90)    

# default arguments
def fun(name,rollno,branch,college):
    print(name,rollno,branch,college="GIET")
fun("subham",11,"CSE")
fun2("PG",12,"CSE")

#right most argument is the default argument
def fun(name,rollno,branch="CSE",college="GIET"):
     print(name,rollno,branch,college="GIET")
fun("subham",11,)
fun2("PG",12,)
fun2("PG",12,"ECE")
# function overloading

def function(*var): # tuple=
    for i in var:
        print(i,end=' ')
# variable no of arguments
function(10,20)
print()
function(10,20,30)
print()
function(10,20,30,40)
print()


def add(*var): # tuple=
    sum = 0
    for i in var:
        sum += i
    return sum
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))



