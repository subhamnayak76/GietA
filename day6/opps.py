
class Account:
    def __init__(self,account_type,balance,min_balance):
        self.__account_type = account_type
        self.__balance = balance
        self.__min_balance = min_balance

    def get_account_type(self):
        return self.__account_type
    def get_balance(self):
        return self.__balance 
    def get_min_balance(self):
        return self.__min_balance
    def set_balance(self,upadate):
        self.__balance = upadate


class OverdrawException(Exception):
    pass
class LimitReachedException(Exception):
    pass
 
class Customer:
    def __init__(self,customer_id,name,age,account):
        self.__customer_id = customer_id
        self.__customer_name =  name
        self.__age = age
        self.account = account

    def take_card(self):
        print("Take card out from the ATM")
    def get_customer_id(self):
        return self.__customer_id
     
    def get_customer_name(self):
        return self.__customer_name
    
    def get_customer_age(self):
        return self.__age

    def withdraw(self,amount):
        if amount > self.account.get_balance():
            raise OverdrawException("cannot withdraw more than that amount balance")
        elif amount 
        
class PrivilegedCustomer:
    def __init__(self,customer_id,customer_name,age,account,bonus_points,amount,name):
        self.__bonus_points = bonus_points
        Customer.__init__(self,customer_id,name,age,amount)
    
    def withdraw(self,amount):
        pass


