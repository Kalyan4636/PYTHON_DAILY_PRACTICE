#parameterized constructors

class student:

    def __init__(self, name):
        print("This is parametrized constructors")
        self.name = name
    def show(self):
        print("hello",self.name)

student = student("python language")
student.show()
