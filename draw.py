import turtle
p = turtle.Turtle()
p.shape('turtle')
p.pensize(5)
p.color('red', 'blue')
p.begin_fill()
for i in range(2):
    p.fd(100)
    p.rt(90)
    p.fd(50)
    p.rt(90)
p.end_fill()
turtle.done()