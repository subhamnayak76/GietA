#list 
list1 =[]
list1 = [10,20,30]
list2 =[10,20.0,True,"paji"]
list3= list([(100.0,200,300,400)])
#append function
list3.append(502)
#extend
list3.extend([7,4,5,"sd"])
list3.insert(4,350)#index,value
list3.remove(502)
# delete last element 
list3.pop()
#delete index
list3.pop(0)
#delete using 
del list3[1]


print(list2)
print(list3)