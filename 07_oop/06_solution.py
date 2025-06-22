# Class Variable
# Add a class variable to Car that keeps track of the number of cars created

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    
    def fullName(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize



# my_tesla = ElectricCar("Tesla", "Roadster", "100kwh")

car1 = Car("Toyota", "Fortuner")
car2 = Car("Toyota", "Fortuner")
car3 = Car("Toyota", "Fortuner")
car5 = Car("Toyota", "Fortuner")
car6 = Car("Toyota", "Fortuner")


print(Car.total_car)