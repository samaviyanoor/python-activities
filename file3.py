
file = open("codingal.txt","r")

print(file.read())

file.close()

file_write=open("codingal.txt","w")

file_write.write("This file is in writable mode")

file_write.write("Hello, how are you")

file_write.close()

file_append=open("codingal.txt","a")

file_append.write("\n")

file_append.write ("We have added in the existing file")

file_append.write ("hi, Good Evening")

file_append.close()