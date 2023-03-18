class Admission:
    def __init__(self):
        self.__st_id = None
        self.__st_marks =None
        self.__st_age = None
        self.__total_amount = None
        self.__fees = None
    def set_validate_marks(self,marks):
        self.__st_marks = marks
        if self.__st_marks >= 0 and self.__marks <= 100:
            return True
        else:
            return False
    def set_validate_age(self,age):
        self.__st_age = age
        if self.__st_age >= 20:
            return True
        else:
            return False
         
    def check_qualification(self):
        if c = set_val:
            if self._st_marks >= 65:
                return self.check_admission()
            else:
                return False
        else:
            print("Not eligible")
    def check_admission(self):
        if self.__st_id == 1001:
            if self.__st_marks >= 85:
                self.__total_amount = 0.75 * 25575
            else:
                self.__total_amount = 25575    
        elif self.__st_id == 1002:
            if self.__st_marks >= 85:
                self._total_amount = 0.75 * 15500
            else:
                self.__total_amount = 15500                
        return self.__total_amount
    def get_value(self):
        return self.__total_amount

s = Admission()
s.set_validate_age(20)
s.set_validate_marks(65)
print(s.get_value())                