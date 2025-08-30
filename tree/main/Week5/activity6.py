
class Student:
    def __init__(self, name, age):
        self.name = name # public​
        self._age = age # protected​
        self.__grade = 'A' # private​
        self.__address = '123 main st' # private​

    def get_address(self):
        return self.__address

    def get_grade(self):
        return self.__grade
    
    # activity 6.2
    def update_grade(self, grade):
        self.__grade = grade

class Info(Student):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_age(self):
        return self._age
    
    def get_name(self):
        return self.name

s = Student('Ali', 20)
info = Info('Joe', 18)

print(s.name) # accessible​
print(s.get_address()) # get private attribute
print(info.get_age()) # get protected attribute
print(info.get_name()) # get public attribute
print(s.get_grade()) # correct way​

# activity 6.2
s.update_grade('A+')
print(s.get_grade())