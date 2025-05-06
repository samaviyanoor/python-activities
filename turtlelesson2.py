import turtle
pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("yellow")



pen.color("green")


pen.circle(50)
pen.left(180)
pen.circle(80)

pen.color("black")

pen.up()
pen.goto(-25,65)
pen.down()
pen.dot(10)


pen.color("black")

pen.up()
pen.goto(25,65)
pen.down()
pen.dot(10)


pen.color("black")

pen.up()
pen.goto(5,45)
pen.down()
pen.dot(10)


pen.color("black")
pen.up()
pen.goto(5,45)
pen.down()
pen.right(-90)
pen.circle(20,180)

screen.mainloop()
