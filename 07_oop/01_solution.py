# Basic class and object
# Create a class with attributes like brand and model. Then create an instance of this class.

# Good practice to be class name Capitalized

# This class is now a blank form
class Car:
    def __init__(self, brand, model): # __inti__ is the constructor
        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corolla")
print(my_car.brand, my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand, my_new_car.model)