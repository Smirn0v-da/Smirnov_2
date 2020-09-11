import turtle
turtle.shape('turtle')
turtle.speed(200)
def okr(x):
    for i in range (100):
        turtle.forward(x)
        turtle.left(3.6)

def dug(y):
    for i in range (50):
        turtle.forward(y)
        turtle.left(3.6)

turtle.penup()
turtle.forward(200)
turtle.left(90)
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()
okr(15)
turtle.end_fill()
turtle.penup()
turtle.color('blue')
turtle.goto(100 , 80)
turtle.begin_fill()
okr(3)
turtle.end_fill()
turtle.penup()
turtle.color('blue')
turtle.goto(-70 , 80)
turtle.begin_fill()
okr(3)
turtle.end_fill()
turtle.width(15)
turtle.penup()
turtle.color('black')
turtle.goto(-35 , 40)
turtle.left(180)
turtle.pendown()
turtle.forward(60)
turtle.penup()
turtle.color('red')
turtle.goto(-170 , -40)
turtle.pendown()
dug(8)


