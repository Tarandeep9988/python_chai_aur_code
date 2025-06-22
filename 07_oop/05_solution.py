# # Setter method
# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model

#     def get_brand(self):
#         return self.__brand
#     def set_brand(self, brand):
#         self.__brand = brand
#     def fullName(self):
#         return f"{self.__brand} {self.model}"

# class ElectricCar(Car):
#     def __init__(self, brand, model, batterySize):
#         super().__init__(brand, model)
#         self.batterySize = batterySize



# my_tesla = ElectricCar("Tesla", "Roadster", "100kwh")

# my_tesla.set_brand("BRD")

# print(my_tesla.get_brand())




# Polymorphism
# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand
    
    def fullName(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def fuel_type(self):
        return "Electric"

my_car = Car("Suzuki", "Swift")
my_tesla = ElectricCar("Tesla", "Roadster", "100kwh")


print(my_car.fuel_type())
print(my_tesla.fuel_type())
# print(my_tesla.get_brand())