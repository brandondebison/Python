#!/usr/local/bin/python3
class Student: 
    #define a constructor
    def  __init__(self):
        super().__init__()

    def __init__(self,id2,name):
        super().__init__()
        self.id = id2
        self.n = name

    def display(self):
        print(self.id, " / ", self.n)

    def setID(self, id2):
        self.id = id2

    def setName(self, name):
        self.n = name

    def getID(self):
        return self.id

    def getName(self):
        return self.n


student2 = Student(1,"hello")
student2.display()
student2.setID(55)
student2.display()

print(student2.getName())