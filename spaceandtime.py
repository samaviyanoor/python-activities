# sum of first n natural numbers
def fun1(n):
    return n * (n + 1) /2
print(fun1(4)) #iterations = 1 most efficient


def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

print(fun2(4)) #iterations = 4


#loop inside a loop
def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum = sum + 1
    return sum

print(fun3(4)) #iterations = 10