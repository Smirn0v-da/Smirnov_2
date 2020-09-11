import turtle
x = 3
y = x
turtle.shape('turtle')
for i in range (1000):
    turtle.forward(0.002 * (1 + y**2)**(1 / 2))
    turtle.left(x)
    y+=x
  


