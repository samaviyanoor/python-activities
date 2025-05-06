fruits = ["mango","apple","banana","berries","watermelon","peach"]
print(fruits)
print(type(fruits))


print(fruits[0])
print(fruits[::-1])
print(fruits[2:5])
print(fruits[0:3])
fruits.append("strawberry")
print(fruits)
fruits.append("apple")
print(fruits)

print(len(fruits))

print(fruits.count("apple"))

fruits[4] = "melon"
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.pop(3)
print(fruits)

fruits.clear()
print(fruits)