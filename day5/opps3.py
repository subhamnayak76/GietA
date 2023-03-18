class Customer:
    def __init__(self,quanity):
        self.quanity = quanity

    def validate_quantity(self):
        if self.quanity >= 1 and self.quanity <= 5:
            return True
        else:
            return False
            
class Pizzaservice:
    def __init__(self,pizza_type,topping):
        self.counter = 100
        self.additional_topping = topping
        self.pizza_type = pizza_type

        #if true if additional_topping is required
    def validate_pizza_type(self):
        if self.pizza_type == "small" or self.pizza_type == "medium":
            return True
        else:
            return False
        
    def calulate_pizza_cost(self,cost,service_id):
        self.service_id = " "
        self.total_cost = cost
        if self.validate_pizza_type() == True:
            self.counter += self.counter + 1
            if self.pizza_type == "small":
                self.total_cost = 150
                if self.pizza_type == "small":
                    self.total_cost += 35
                self.service = str(self.counter) + "S"
            elif self.pizza_type == "medium":
                self.total_cost = 200
                if self.additional_topping == "True":
                    self.total_cost += 50
                self.service = str(self.counter) + "M"
        else:
            self.total_cost = -1


class Doordelivery:
    def __init__(self,distance):
        self.distance = distance
        self.validate_distance_kms(self)

    def validate_distance_kms(self):
        if self.distance > 0 and self.distance< 10:
            return True
        else:
            return False



        #acces the quanity to customer class
