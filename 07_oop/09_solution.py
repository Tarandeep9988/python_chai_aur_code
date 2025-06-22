# Class Inheritance and isinstance() Function
# Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar

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



my_car = Car("Toyota", "Fortuner")

my_tesla = ElectricCar("Tesla", "Roadster", "100kwh")

print(isinstance(my_tesla, Car))
print(isinstance(my_car, ElectricCar))

