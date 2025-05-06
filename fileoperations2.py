with open("technology.txt","r") as q:
    data=q.readlines()
    for i in data:
        word = i.split()
        print(word)

q.close()


with open("myfile.txt", "w") as f:
    f.write("today is tuesday and it is raining")

f.close()



