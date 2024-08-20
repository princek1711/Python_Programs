''' Basic Class, Object and Inheritance'''

# Creating a class named Car
class Car:
    # Initializing a Car object with brand and model attributes
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Defining a method to return the full name of the car
    def full_name(self):
        return f"{self.brand} {self.model}"

# Creating a new class named ElectricCar that inherits from Car
class ElectricCar(Car):
    # Initializing an ElectricCar object with brand, model,
    #  and battery size attributes
    def __init__(self, brand, model, battery_size):
        # Calling the initializer of the parent class Car
        super().__init__(brand, model)  
        self.battery_size = battery_size

# Creating an instance of ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", "85 kWh")

# Printing the brand, model, and battery size of the electric car
print(my_electric_car.brand, my_electric_car.model, my_electric_car.battery_size)

# Printing the full name of the electric car using the method from the Car class
print(my_electric_car.full_name())

# my_car = Car("Toyota, ", "Fourtuner")
# print(my_car)
# print(my_car.brand,my_car.model)
# print(my_car.full_name())
# my_new_car = Car("Honda, ","City")
# print(my_new_car.brand, my_new_car.model)



 