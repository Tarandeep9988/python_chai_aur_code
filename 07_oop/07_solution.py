# Static method
# Add a static method to the Car class that returns a general description of a car



class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    
    def fullName(self):
        return f"{self.brand} {self.model}"
    
    # Static method
    @staticmethod # @staticmethod is called a decorator and enhance the functionality of method
    def general_description():
        return "Cars are means of transport"

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

myCar = Car("Toyota", "Fortuner")

print(Car.general_description())