import turtle
import math

def mn(n , r)
    turtle.forward(r)
    turtle.left(90 + 180 / n)
    x = 2 * r * math.sin( math.pi / 2)
    for i in range (n):
        turtle.forward(x)
        turtle.left(360 / n)
    turtle.left(90 - 180 / n)
    turtle.forward(r)
    turtle.left(180)

    
    
        
        
    
    


