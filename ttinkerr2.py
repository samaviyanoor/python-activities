from tkinter import *

root = Tk()

root.title("class a grades")
root.geometry("400x250")
root.config(bg="lavender")

heading = Label(root, text="class a grades", font=("rial",20))
name = Label(root, text="name", font=("arial",10))
enterybox = Entry(root,)
grade = Button(root, text="submit", font=("arial",10))

name.place(x=100,y=60)
grade.place(x=100,y=100)
heading.place(x=100,y=5)
enterybox.place(x=150,y=60)


frame1 = Frame(master=root, borderwidth=10, bg="green")
frame1.place(x=100,y=200)

label1 = Label(frame1, text="first frame")
label1.pack()
root.mainloop()

