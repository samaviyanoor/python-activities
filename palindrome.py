#Palindrone number 

num = int(input("enter a number "))


original = num 
reverse = 0

while num>0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse :
    print("it is a palindrome")

else:
    print("it is not a palindrome")