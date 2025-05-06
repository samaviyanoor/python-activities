file = open("condingal.txt")

print(file.read())

file.close()

file_write = open("condingal.txt","w")
file_write.write("this file is in writable mode")
file_write.write("hello, how are you?")
file_write.close()



file_append = open("condingal.txt", "a")
file_append.write("\n")
file_append.write("we have added in the existing file")
file_append.write("mam renuka looks pretty")
file_append.close()