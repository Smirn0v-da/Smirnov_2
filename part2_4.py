import turtle as t
x, y, dt ,Vx ,Vy ,ay = -350, 0, 0.05, 15 ,50 , -10

t.goto(350 , 0)
t.goto(-350, 0)
for i in range (700):
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    if y <= 0:
        Vy = -0.8*Vy 
    t.goto(x, y)
