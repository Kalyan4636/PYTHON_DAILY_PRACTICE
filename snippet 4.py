class Vehicle:
 def __init__(self, brand):
 self.brand = brand
 def drive(self):
 return "Vehicle is driving"
class Car(Vehicle):
 def __init__(self, brand, model):
 super().__init__(brand)
 self.model = model
 def drive(self):
 return "Car is driving"
