class Computer:
    def __init__(self):
        self.__price=900
        
    def sell(self):
        print(self.__price)

    def changeprice(self,price):
        self.price=price

comp=Computer()
comp.sell()
comp.changeprice(1000)
comp.sell()

class Square:
    def __init__(self):
        self.__side=10
    
    def area(self):
        print("the side is",self.__side)
        print("the area of the square is", self.__side*self.__side)

sq=Square()
sq.__side=15
sq.area()