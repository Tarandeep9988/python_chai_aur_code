# Encapsulation
# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it


class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand
    
    def fullName(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize



my_tesla = ElectricCar("Tesla", "Roadster", "100kwh")

print(my_tesla.get_brand())

# variable starting with __ (double underscore) are private