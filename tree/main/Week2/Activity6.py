# You are tasked with developing a simple program for the Human Resources (HR) department 
# to store and display basic employee information, including each employee’s name, salary, and job title.
# Requirements:
# Create at least two Employee objects with different data.
# Call the display_info() method to show each employee’s details.
# Call the give_raise() method to increase an employee’s salary and display the updated amount.

class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title
    
    def display_info(self):
        return f"name: {self.name}\nsalary: {self.salary}\njob title: {self.job_title}\n"
    
    def give_raise(self, salary):
        self.salary = salary
        return f"name: {self.name}\nsalary: {self.salary}\njob title: {self.job_title}\n"

def main():
    employee1 = Employee("Mark", 2000, "manager") 
    employee2 = Employee("Rose", 1000, "waitress") 

    print(Employee.display_info(employee1))
    print(Employee.display_info(employee2))

    raise_salary = input("increase Mark's salary: ")
    print(employee1.give_raise(raise_salary))

if __name__ == "__main__":
    main()