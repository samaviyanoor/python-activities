class Mobile:
   def __init__(self):
     print("constructor is called and object is created")
     
     def __del__(self):
        print("destructor called and object is deleted")

iphone=Mobile()
del iphone