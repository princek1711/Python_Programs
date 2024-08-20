'''Encapsulation'''

#Problem: Modify the Car class to encapsulate the brand attribute,
# making it private, and provide a getter method for it.

#Creating a class name Car
class Car:
    #Defining a car object with brand and model
    def __init__(self,__brand,__model): 
        self.set_brand(__brand) 
        self.set_model(__model) 

    #Definig setter and getter method to make brand model name private
    def get_brand(self):    
        return self.__brand
    
    def set_brand(self,value):
        if not value:
            raise ValueError("Brand name can't be empty") 
        self.__brand = value

    def get_model(self):        
        return self.__model

    def set_model(self,value):    
        if not value:
            raise ValueError("Model name can't be empty") 
        self.__model = value    

    #Defining a method to return full name
    def full_details(self):   
        return f"{self.__brand} {self.__model}"

#Asking from user for brand and its model name
brandName = input("Enter brand name of the car...")
modelName = input("Enter model of that brand....")


#Creating a veriable to store brand name and model name
my_car=Car(brandName,modelName) 
#Printing brand name individually
print(my_car.get_brand())
#Printing full details 
print(my_car.full_details())
        













