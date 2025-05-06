class Library:
  def __init__(self, booklist,name):
    self.booklist=booklist
    self.name=name
    self.lenddict={}

  def displaybooks(self): 
    print("we have the following books in the library")
    
    for i in self.booklist:
        print(i)
        
  def lendbook(self, user, book):
    self.lenddict.update({book:user})
    print("the record has been updated")
          
          
  def addbook(self, book):
    self.booklist.append(book)
    print("the book has been added in the records")
            
  def returnbook(self,book):
    self.lenddict.pop(book)


books = Library(["python","harry potter"],"lets upskill")

while True:
  print("welcome to Upskill library")
  print("1- display books")
  print("2- lend a book")
  print("3- add a book")
  print("4- return book")
  print("5- quit")
  
  userchoice= int(input("select from the list, what to do. "))

  if userchoice == 1:
    books.displaybooks()
    
  elif userchoice == 2: 
    book = input("which book do you want to lend? ")
    user = input("enter your name ")

    books.lendbook(user,book)

  elif userchoice == 3:
    book = input("which book do you want to add to the library")

    books.addbook(book)

  elif userchoice == 4:
    book = input("which book do you like to return to the library")
    books.returnbook(book)
  elif userchoice == 5:
    exit()
