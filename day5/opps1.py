class Vehicles:
    def __init__(self,vehicle_cost,vehicle_type):
        self.__vehicle_cost =vehicle_cost
        self.__vehicle_type = vehicle_type
        self.__premium_amount = None
        
    def set_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = self.__vehicle_cost * (2/100)
        elif self.__vehicle_type =="Four Wheeler":
            self.__premium_amount = self.__vehicle_cost * (6/100)
        else:
            self.__premium_amount = "Error"

    def get_vehcile_type(self):
        return self.__vehicle_type
     
    def get_vehicle_cost(self):
        return self.__vehicle_cost
     
    def get_premium(self):
        return self.__premium_amount

v = Vehicles(2000,"Two Wheeler")
v.set_premium()

print("vehicle type : ",v.get_vehcile_type())
print("vehicle cost :",v.get_vehicle_cost())
print("vehicle premium :",v.get_premium())  
