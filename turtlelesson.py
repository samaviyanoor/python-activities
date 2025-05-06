import turtle

pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("green")

pen.color("yellow")
pen.begin_fill()


for i in range(4):
   pen.forward(150)
   pen.right(90)


pen.end_fill()
screen.mainloop()