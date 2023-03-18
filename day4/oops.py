class Example:
    def __init__(self,num):
        self.num= num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num    
obj = Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())


#2
class Customer:
    def __init__(self):
        cust_id = 100

c1 = Customer()
print(c1.cust_id) 
# it will show error as there is not instance variable


#3
class Customer:
    def__init__(self,id):
        self.id= 100
c1 = Customer(200)
print(c1.id) 

#4
class Customer:
    def__init__(self,id):
        self.id= id
c1 = Customer(200)
print(c1.id)

