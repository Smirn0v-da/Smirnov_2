import turtle

def okr(x):
    for i in range (100):
        turtle.forward(x)
        turtle.left(3.6)

n = 6
for i in range (n):
    okr(5)
    turtle.left(360 / n)
    
