from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.title("image")
root.geometry("400x400")

upload= Image.open("reverse 1999.jpg")

image = ImageTk.PhotoImage(upload)

label1 = Label(root, image=image,height=250, width=300)
label1.place(x=50,y=10)

label2= Label(root, text="this is how we can add image in Tkinter window")
label2.place(x=70, y=320)

root.mainloop()