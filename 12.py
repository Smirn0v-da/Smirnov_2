import turtle

def dug(x):
    for i in range (50):
        turtle.forward(x)
        turtle.left(3.6)

n = 3
for i in range (n):
    dug(3)
    dug(0.5)
