number = int(input("enter a number"))


result = 0 
temp = number 
while temp !=0:
    digit =temp % 10
    result = result + digit **3
    temp = temp // 10

print(result)

if number == result:
    print(number, "it is an armstrong number ")
else:
    print("it is not an armstrong number ")
