class Compartment:
    def __init__(self,name,capacity,no_of_passenger):
        self.name = name
        self.capacity = capacity
        self.no_of_passenger = no_of_passenger

class Train:
    def __init__(self,train_name,compartment_list):
        self.train_name = train_name
        self.compartment = compartment_list
        self.head = None

    def get_train_name(self):
        return self.train_name

    def get_compartment_list(self):
        pass

    def count_compartments(self):
       if self.head is None:
            print("the list of has no element ")
            return
        n = self.head
        count = 0
        while n is not None:
            count = count + 1
            n = n.ref
        return count               