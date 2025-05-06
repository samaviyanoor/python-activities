from tkinter import *

root = Tk()

root.title("my first tkinter window")
root.geometry("400x250")
root.config(bg="lavender")
heading = Label(root , text = "students introduction",bg="pink",height=2,width=20,fg="white",font=("Arial,20"))
button1 = Button(root, text = "click", bg="maroon",height=1,width=10,fg="white")
name = Label(root, text="enter your name", bg="pink",height=1,width=10,fg="white")
entery1 = Entry(root)

heading.pack()
button1.pack()
name.pack()
entery1.pack()


root.mainloop()