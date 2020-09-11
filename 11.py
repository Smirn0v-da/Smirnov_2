import turtle

def okr(x):
    for i in range (100):
        turtle.forward(x)
        turtle.left(3.6)

d = 3
n = 5
for i in range (n):
    okr(d)
    turtle.left(180)
    okr(d)
    turtle.left(180)
    d +=1
    

        
