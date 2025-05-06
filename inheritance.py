#parent class:
class Person():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def display(self):
        print(self.name)
        print(self.id)

#child class:

class Employee(Person):
    def __init__(self,name,id,salary,designation):
        Person.__init__(self,name,id)
        self.salary=salary
        self.designation=designation
        

atharv= Employee("atharvB","B001",1000000,"VP")
atharv.display()

samaviya= Employee("samaviyaN","B002",2000000,"SVP")
samaviya.display()