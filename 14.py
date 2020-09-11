import turtle

def zv(n , l):
    for i in range (n):
        turtle.forward(l)
        turtle.left(180 - 180 / n)

zv(5 , 100)
turtle.penup()
turtle.forward(200)
turtle.pendown()
zv(11 , 100)
    
    
    
