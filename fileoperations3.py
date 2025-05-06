import os 
if os.path.exists("myfile.txt"):
    print("file exists on your system")
    os.remove("myfile.txt") 

else:
    print("file does not exist on your system")