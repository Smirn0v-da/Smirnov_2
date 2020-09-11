import turtle

turtle.shape('turtle')
x=5
for j in range (10):
    for i in range (4):
        turtle.forward(x)
        turtle.left(90)
    turtle.right(90)
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.pendown()
    turtle.left(180)
    x+=10
    

    


