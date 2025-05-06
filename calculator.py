def addition(number_1,number_2):
    print(number_1 + number_2)

def multiplication(number_1,number_2):
  print(number_1 * number_2)

def subtraction(number_1,number_2):
    print(number_1 - number_2)

def division(number_1,number_2):
   print(number_1 / number_2)


number_1 = int(input("please enter the first number"))
number_2 = int(input("please enter the second number"))

calculation = int(input("now choose which operation you want to do, enter 1 for addition, enter 2 for substraction, enter 3 for multiplication and enter 4 for division"))


if calculation == 1:
    addition(number_1,number_2)

elif calculation == 2:
    subtraction(number_1,number_2)

elif calculation == 3:
    multiplication(number_1,number_2)

elif calculation == 4:
    division(number_1,number_2)


