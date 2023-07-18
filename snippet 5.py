class Parent:
 def __init__(self, name):
 self.name = name
 def get_name(self):
 return self.name
class Child(Parent):
 def __init__(self, name, age):
 super().__init__(name)
 self.age = age
parent = Parent("Priya")
child = Child("Priti", 10)
result1 = parent.get_name()
result2 = child.get_name()
print(result1, result2)
