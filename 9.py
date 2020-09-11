import turtle
import math

def mn(n , r):
    turtle.penup()
    turtle.forward(r)
    turtle.pendown()
    turtle.left(90 + 180 / n)
    x = 2 * r * math.sin( math.pi / n)
    for i in range (n):
        turtle.forward(x)
        turtle.left(360 / n)
    turtle.left(90 - 180 / n)
    turtle.penup()
    turtle.forward(r)
    turtle.left(180)

a = 3
b = 40
for i in range(10):
    mn(a , b)
    a += 1
    b += 20


    
    
        
        
    
    


