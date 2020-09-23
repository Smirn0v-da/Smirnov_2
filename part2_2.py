import turtle as t
t.shape('turtle')
t.width(5)

p0 = [(0, 0), (50, 0), (50, 100), (0, 100), (0, 0)]
p1 = [(50 , 0), (50, 100), (0, 50)]
p4 = [(50, 0), (50, 100), (50, 50), (0, 50), (0, 100)]
p7 = [(0, 0), (0, 50), (50, 100), (0, 100)]

x = -350
y = 0

t.up()
t.goto(x + p1[0][0],y + p1[0][1])
t.down()
for i,j in p1:
    t.goto(x + i, y + j)
x += 100

t.up()
t.goto(x + p4[0][0],y + p4[0][1])
t.down()
for i,j in p4:
    t.goto(x + i, y + j)
x += 100

t.up()
t.goto(x + p1[0][0],y + p1[0][1])
t.down()
for i,j in p1:
    t.goto(x + i, y + j)
x += 100

t.up()
t.goto(x + p7[0][0],y + p7[0][1])
t.down()
for i,j in p7:
    t.goto(x + i, y + j)
x += 100

t.up()
t.goto(x + p0[0][0],y + p0[0][1])
t.down()
for i,j in p0:
    t.goto(x + i, y + j)
x += 100

t.up()
t.goto(x + p0[0][0],y + p0[0][1])
t.down()
for i,j in p0:
    t.goto(x + i, y + j)
x += 100 
    
    
    
