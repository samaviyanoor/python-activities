from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("cash tally")
root.geometry("700x700")

upload= Image.open("cash tally.png")

image = ImageTk.PhotoImage(upload)

label1 = Label(root, image=image,height=450, width=400)
label1.place(x=150,y=10)

label2 = Label(root, text="hey user, welcome to denomination counter", bg="lavender")
label2.place(x=200, y=500)



def welcome():
    message = messagebox.showinfo("Alert!","do you want to calculate the denomination?")
    if message == "ok":
        top_window()

        
button1 = Button(root, text="lets get started", bg="orange", command=welcome)
button1.place(x=200,y=600)


def top_window():
    top = Toplevel()
    top.geometry("500x500")
    top.title("denominations calculator")
    label5 = Label(top, text="calculate the denomination here")
    label5.pack()
    label3 = Label(top, text="enter the total amount")
    entrybox = Entry(top)
    label4 = Label(top, text="here are the number of notes for each denomination")
    label3.place(x=200,y=100)
    entrybox.place(x=350,y=100)
    label4.place(x=200,y=150)
    fifty = Label(top, text=50)
    hundred = Label(top, text=100)
    five_hundred = Label(top, text=500)
    entry_fifty = Entry(top)
    entry_hundred = Entry(top)
    entry_fivehundred = Entry(top)
    fifty.place(x=250,y=250)
    hundred.place(x=250,y=350)
    five_hundred.place(x=250,y=450)
    entry_fifty.place(x=350,y=250)
    entry_hundred.place(x=350,y=350)
    entry_fivehundred.place(x=350,y=450)
    top.mainloop()

root.mainloop()