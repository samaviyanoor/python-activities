# O(n)Time:
def ontime(n):
    j=0
    for i in range(1,n+1):
        j +=1
    print("the number of iterations are ", j)

ontime(10)
ontime(20)

print("with every change in n, iterations will also change, whereby affeting the time taken to run the code")


