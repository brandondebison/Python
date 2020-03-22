#!/usr/local/bin/python3

class Employee:
    empCount = 0
    def __init__(self,name,salary):
        super().__init__()
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("We have ", Employee.empCount, " employees")

    def display(self):
        print("Name: ", self.name,"/Salary: ", self.salary)


emp1 = Employee("Brandon", 20)
emp2 = Employee("Brandon2", 22)

emp1.display()
emp2.display()
emp1.displayCount()
emp2.displayCount()
emp1.


class Boss(Employee):
    def __init__(self, name, salary,position):
        super().__init__(name, salary)
        self.position = position
        self.__hiddenposition = "hidden position" #this is how to hide the data

    def getHiddenPosition(self):
        return(self.__hiddenposition) # if you need to get access you need to create the getter

emp3 = Boss("boss",23,"Manager")
emp3.displayCount()
print(emp3.position)
print(emp3.getHiddenPosition())
