from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Alert")
root.geometry("400x400")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found!")

button1 = Button(root, text="scan for virus", command=msg)
button1.place(x=150, y=80)
root.mainloop()
