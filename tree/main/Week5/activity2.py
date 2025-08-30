class Person():
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age
    
    def greet(self):
        print("Hello " + self.name)
        
    
class Academic(Person):
    def __init__(self, name, address, age, salary):
        super().__init__(name, address, age)
        self.salary = salary

class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        self.student_id = student_id

    def update(self, name, address, age, student_id):
        self.name = name
        self.address = address
        self.age = age
        self.student_id = student_id

    def greet(self):
        print("Good morning " + self.name)

student1 = Student("Alice", "123 main st", 20, "S12345")
student1.update("Alice Wang", "123 main st", 20, "S12345")
student1.greet()