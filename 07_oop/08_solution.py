# Property Decorators
# Use a property decorator in the Car class to make the model attribute read-only

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model

myCar = Car("Toyota", "Fortuner")

# myCar.__model = "Land Cruiser"
# print(myCar.__model)
print(myCar.model)