import turtle as t
from random import *

t.up()
t.goto(-250, 250)
t.down()
for i in range (4):
    t.forward(500)
    t.right(90)
    
number_of_turtles = 20

pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.turtlesize(0.5, 0.5)
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.seth(randint(0, 360))

while True:
    for unit in pool:
        unit.forward(randint(1, 5))
        if abs(unit.xcor()) >= 250:
            unit.seth(180 - unit.heading())
            unit.forward(5)
        if abs(unit.ycor()) >= 250:
            unit.seth(360 - unit.heading())
            unit.forward(5)
