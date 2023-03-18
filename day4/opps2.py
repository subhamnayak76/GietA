# class Book:
#     def __init__(self):
#         self.title=None
# my_fav = Book()
# my_fav.title ="Head First Programing"
# your_fav = Book()
# your_fav.title = "learn Python the hard way"

# my_fav.title="learning python"
# print("my favorite is ",my_fav.title)
# print("my favorite is ",your_fav.title)


# class Shoe:
#     def __init__(self,price,material):
#         self.price = price
#         self.material = material

# s1 = Shoe(1000,"canvas")
# print(s1) 
# print(s1.price,s1.material)
# it will the print address        

'''class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material

s1 = Shoe(1000,"canvas")
print(s1) 
print("the unique id of the object",id(s1))
s2 = Shoe(200,"cotton")
print("the unique id of the object",id(s2))
'''


# class Shoe:
#     def __init__(self,price,material):
#         self.price = price
#         self.material = material
#     def __str__(self):
#         return "Shoe with price :" + str(self.price) + " and material: " + self.material
       

# s1 = Shoe(1000,"canvas")
# print(s1)

# class Mobile:
#     def __init__(self):
#         print(id(self))

#     def display(self):
    
#         print("displaying details")

#     def purchase(self):
#         self.display()
#         print("calculating price")

# # Mobile().purchase() 

# m1 = Mobile()
# print(m1)
# m2 = Mobile()
# print(m2)




# class Mobile():
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
#         self.total_price = None
#     def purchase(self):
#         if self.brand == "Apple":
#             discount = 10
#         else:
#             discount = 5
#         self.total_price = self.price - self.price * (discount /100)

#         # print("total price of" ,self.brand,"mobile is",self.total_price)
#         # return self.total_price
#     def actual(self):
#         return (self.price-self.total_price)    

# mob1 = Mobile("Apple",20000)
# mob2 = Mobile("Samsung",10000)
# mob1.purchase()
# mob2.purchase()

# print(mob1.actual())



# class Customer:
#     def __init__(self ,cust_id,name,age,wallet_balance):
#         self.cust_id = cust_id
#         self.name = name
#         self.age = age
#         self.__wallet_balance = wallet_balance
#     def upadate_balance(self,amount):
#         if amount < 1000 and amount > 0:
#             self.__wallet_balance += amount
#     def show_balance(self):
#         print("The balance is",self.__wallet_balance)
# cus = Customer(100,"gopal",18,2000)
# cus.upadate_balance(500)
# cus.show_balance()
# print(cus.__wallet_balance)

#how to acces the private wallet balance
#using setter and getter

# class Customer:
#     def __init__(self ,cust_id,name,age,wallet_balance):
#         self.cust_id = cust_id
#         self.name = name
#         self.age = age
#         self.__wallet_balance = wallet_balance
#     def set_balance(self,amount):
#         if amount < 50000 and amount > 0:
#             self.__wallet_balance += amount
#     def show_balance(self):
#         print("The balance is",self.__wallet_balance)
#     def get_wallet_balance(self):
#         return self.__wallet_balance    
# cus = Customer(100,"gopal",18,2000)
# # cus.upadate_balance(500
# # print(cus.__wallet_balance)
# print(cus.get_wallet_balance())
# cus.set_balance(5000)
# print(cus.get_wallet_balance())


# class Dam:
#     def __init__(self,name,length):
#         self.name = name
#         self.__length =length
#     def get_length(self):
#         return self.__length 

# d = Dam("ABC dam",3.5)
# print("Dam name is",d.name)
# print("Dam Length",d.get_length())       


# class Table:
#     def __init__(self):
#         self.no_of_leg = 4
#         self.__glass_top = None
#         self.__wooden_top =None
#     def assign_data(self,glass_top,wooden_top):
#         self.__glass_top = glass_top
#         self.   






class Table:
    def __init__(self):
        self.no_of_legs = 4
        self.glass_top = None
        self.wooden_top = None
dining_table = Table()
Back_table = Table()
front_table = Back_table
print(Back_table,front_table,dining_table)

# class Customer:
#     def __init__(self ,cust_id,name,age,wallet_balance):
#         self.cust_id = cust_id
#         self.name = name
#         self.age = age
#         self.__wallet_balance = wallet_balance
#     def upadate_balance(self,amount):
#         if amount < 1000 and amount > 0:
#             self.__wallet_balance += amount
#     def show_balance(self):
#         print("The balance is",self.__wallet_balance)
# cus = Customer(100,"gopal",18,2000)
# cus.upadate_balance(500)
# cus.show_balance()
# print(cus.__wallet_balance)