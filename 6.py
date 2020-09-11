import turtle

turtle.shape('turtle')
line = input()
n = int(line)
for i in range (n):
    turtle.forward(50)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(50)
    turtle.right(180-360/n)

    


