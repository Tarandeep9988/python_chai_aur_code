# Class Method and Self
# Add a method to the Car class that displays the full name of the class(brand and model)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullName(self):
        return f"{self.brand} {self.model}"


myCar = Car("Suzuki", "Brezza")
print(myCar.fullName())