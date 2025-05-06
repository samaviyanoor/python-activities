#O(n^2)

def onsquaretime(n):
    j=0
    for i in range(1,n):
        for k in range(1,n):
            print("*", end=" ")
            j +=1
        print()
    print("the number of iterations are ", j)

onsquaretime(12)

print("with every change in n, the time taken equals n square")

