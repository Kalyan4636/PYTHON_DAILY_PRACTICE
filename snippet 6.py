class Person:
 def __init__(self, name):
 self.name = name
 def get_name(self):
 return self.name
class Student(Person):
 def __init__(self, name, grade):
 super().__init__(name)
 self.grade = grade
 def get_grade(self):
 return self.grade
student = Student("Priya", 9)
result1 = student.get_name()
result2 = student.get_grade()
print(result1, result2)
