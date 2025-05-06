class Family:
  def __init__(self, name,age,gender,relation):
    self.name = name
    self.age = age
    self.gender = gender
    self.relation = relation
  
  def together(self):
    print("our family eats together")



son = Family("Atharv","12","male","son",)

daughter = Family("Samaviya","15","female","daughter")

father = Family("abcd",35,"male","father")

print(son.name)
print(daughter.age)
father.together()
print(son.age)


our_family = []
our_family.append(son)
our_family.append(daughter)
our_family.append(father)

for i in our_family:
   print(i.name, i.age, i.relation)