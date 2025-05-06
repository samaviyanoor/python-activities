def binarytodecimal(binary):
    decimal = 0
    i = 0
    
    
    while binary !=0:
        dec = binary % 10
        decimal = decimal + dec * pow(2,i)
        binary=binary // 10
        i=i+1
    
    print("the original number is " , decimal)

binary = int(input("enter your binary numbner "))
binarytodecimal(binary)