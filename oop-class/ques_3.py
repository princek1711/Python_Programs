

class newCar:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_details(self):
        return f"{self.brand}{self.model}"
    
    @staticmethod
    def carNumber():
        return f"BR 01 0A 2014"


my_car = newCar("Tesla ","s28")
print(my_car.full_details())
print(newCar.carNumber())
        