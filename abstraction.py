class Animal: 
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("i can walk and run")

class Snake(Animal):
    def move(self):
        print("i can slither")


class Dog(Animal):
    def move(self):
        print("i can bark")

class Lion(Animal):
    def move(self):
        print("i can roar")


man=Human()
man.move()

cobra=Snake()
cobra.move()

husky=Dog()
husky.move()

white_lion=Lion()
white_lion.move()

