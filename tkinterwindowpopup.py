from tkinter import *

root = Tk()
root.title("pop up window")
root.geometry("300x400")

def window_popup():
    top = Toplevel()
    top.geometry("100x400")
    top.title("new window")
    label1 = Label(top, text="welcome to the new window")
    label1.pack()
    top.mainloop()

button1 = Button(root, text="click here to open another window", command=window_popup)
button1.pack()

root.mainloop()