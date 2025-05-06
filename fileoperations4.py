#reading the data from newfile file
with open("newfile.txt") as s:
    data1=s.read()

#reading data from myfile file
with open("myfile.txt") as m:
    data2=m.read()

#merging both the files

data1 +="\n"
data1 += data2

print("merging the files...")

with open("merged.txt","w") as a:
    a.write(data1)