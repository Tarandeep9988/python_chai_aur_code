# Multiple inheritance
# Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance

class Car:
    def __init__(self, brand, model): # __inti__ is the constructor
        self.brand = brand
        self.model = model


class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCar(Battery, Engine, Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)


my_tesla = ElectricCar("Tata", "Harrier EV")


print(my_tesla.battery_info())
print(my_tesla.engine_info())