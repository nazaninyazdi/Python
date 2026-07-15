import turtle
import random

screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgcolor("#FFF8DC")
screen.title("Happy Birthday")

screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_rectangle(x, y, width, height, fill):

    t.penup()
    t.goto(x, y)
    t.setheading(0)

    t.color("black")
    t.fillcolor(fill)

    t.pendown()

    t.begin_fill()

    for i in range(2):
        t.forward(width)
        t.left(90)

        t.forward(height)
        t.left(90)

    t.end_fill()

def draw_circle(x, y, radius, color):

    t.penup()
    t.goto(x, y)

    t.color("black")
    t.fillcolor(color)

    t.pendown()

    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_star(x, y, size):

    t.penup()
    t.goto(x, y)

    t.color("gold")

    t.pendown()

    for i in range(5):
        t.forward(size)
        t.right(144)


for i in range(80):

    x = random.randint(-480, 480)
    y = random.randint(100, 330)
    s = random.randint(6, 12)

    draw_star(x, y, s)

screen.update()

draw_rectangle(
    -220,
    -200,
    440,
    80,
    "#D2691E"
)

draw_rectangle(
    -170,
    -120,
    340,
    70,
    "#FFC0CB"
)

draw_rectangle(
    -120,
    -50,
    240,
    60,
    "#FFF0F5"
)

screen.update()

def draw_cream(x, y):

    t.penup()
    t.goto(x, y)

    t.color("white")
    t.fillcolor("white")

    t.pendown()

    t.begin_fill()

    t.circle(8, 180)

    t.left(180)

    t.end_fill()

    t.setheading(0)



for x in range(-210, 211, 20):
    draw_cream(x, -120)

for x in range(-160, 161, 20):
    draw_cream(x, -50)

for x in range(-110, 111, 20):
    draw_cream(x, 10)

cherries = [
    (-70, 30),
    (-20, 35),
    (30, 30),
    (80, 35)
]

for x, y in cherries:

    draw_circle(
        x,
        y,
        7,
        "red"
    )


colors = [
    "yellow",
    "cyan",
    "orange",
    "lime",
    "magenta",
    "deepskyblue"
]

positions = [
    (-180,-85),
    (-120,-85),
    (-60,-85),
    (0,-85),
    (60,-85),
    (120,-85),
    (180,-85)
]

for i in range(len(positions)):

    x = positions[i][0]
    y = positions[i][1]

    draw_circle(
        x,
        y,
        5,
        random.choice(colors)
    )

age = 3

def draw_candle(x, y, color):

    t.penup()
    t.goto(x, y)

    t.setheading(0)

    t.color("black")
    t.fillcolor(color)

    t.pendown()

    t.begin_fill()

    for i in range(2):

        t.forward(15)
        t.left(90)

        t.forward(45)
        t.left(90)

    t.end_fill()

def draw_flame(x, y):

    t.penup()
    t.goto(x, y)

    t.color("orange")
    t.fillcolor("yellow")

    t.setheading(0)

    t.pendown()

    t.begin_fill()

    t.circle(6)

    t.end_fill()


start_x = -(age * 10) // 2

for i in range(age):

    x = start_x + i * 20

    draw_candle(
        x,
        10,
        random.choice([
            "red",
            "blue",
            "green",
            "purple",
            "pink",
            "cyan",
            "orange"
        ])
    )

    draw_flame(
        x + 7,
        58
    )

def draw_balloon(x, y, color):

    t.penup()
    t.goto(x, y)

    t.setheading(0)

    t.color("black")
    t.fillcolor(color)

    t.pendown()

    t.begin_fill()

    for i in range(2):
        t.circle(25, 90)
        t.circle(50, 90)

    t.end_fill()

    t.penup()
    t.goto(x, y - 50)

    t.setheading(-90)

    t.pendown()

    for i in range(20):

        if i % 2 == 0:
            t.left(15)
        else:
            t.right(15)

        t.forward(5)

    t.penup()

def draw_gift(x, y):

    t.penup()
    t.goto(x, y)

    t.setheading(0)

    t.color("black")
    t.fillcolor("red")

    t.pendown()

    t.begin_fill()

    for i in range(4):
        t.forward(90)
        t.left(90)

    t.end_fill()

    t.penup()
    t.goto(x + 45, y)

    t.setheading(90)

    t.color("gold")

    t.pendown()
    t.forward(90)

    t.penup()
    t.goto(x, y + 45)

    t.setheading(0)

    t.pendown()
    t.forward(90)

    t.penup()
    t.goto(x + 45, y + 90)

    t.setheading(150)

    t.begin_fill()

    for i in range(2):
        t.circle(15, 210)
        t.left(150)

    t.end_fill()

draw_gift(250, -200)

colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "cyan"
]

positions = [
    (-420,220),
    (-330,170),
    (-250,250),
    (250,250),
    (330,170),
    (420,220)
]

for x, y in positions:

    draw_balloon(
        x,
        y,
        random.choice(colors)
    )

def balloon_shine(x, y):

    t.penup()

    t.goto(x + 12, y + 55)

    t.dot(8, "white")

for x, y in positions:

    color = random.choice(colors)

    draw_balloon(
        x,
        y,
        color
    )

    balloon_shine(
        x,
        y
    )

def draw_gift(x, y, color):

    t.penup()
    t.goto(x, y)

    t.setheading(0)

    t.color("black")
    t.fillcolor(color)

    t.pendown()

    t.begin_fill()

    for i in range(4):
        t.forward(90)
        t.left(90)

    t.end_fill()

    t.penup()
    t.goto(x + 45, y)

    t.setheading(90)

    t.color("gold")

    t.pendown()
    t.forward(90)

    t.penup()
    t.goto(x, y + 45)

    t.setheading(0)

    t.pendown()
    t.forward(90)

    t.penup()
    t.goto(x - 5, y + 90)

    t.setheading(25)

    t.fillcolor("gold")

    t.begin_fill()

    t.circle(18, 220)
    t.left(140)
    t.circle(18, 220)

    t.end_fill()

    t.penup()
    t.goto(x + 50, y + 90)

    t.setheading(155)

    t.begin_fill()

    t.circle(18, 220)
    t.left(140)
    t.circle(18, 220)

    t.end_fill()

    t.penup()

draw_gift(250, -200, "red")
draw_gift(-360, -200, "deepskyblue")

def candy(x, y, color):

    t.penup()
    t.goto(x, y)

    t.color("black")
    t.fillcolor(color)

    t.pendown()

    t.begin_fill()
    t.circle(8)
    t.end_fill()

    t.penup()

    t.goto(x - 15, y + 8)

    t.setheading(180)

    t.pendown()

    t.forward(12)

    t.left(35)

    t.forward(8)

    t.backward(8)

    t.right(70)

    t.forward(8)

    t.penup()

    t.goto(x + 15, y + 8)

    t.setheading(0)

    t.pendown()

    t.forward(12)

    t.left(35)

    t.forward(8)

    t.backward(8)

    t.right(70)

    t.forward(8)

    t.penup()

candy(-250, -170, "hotpink")
candy(-220, -190, "orange")
candy(170, -180, "lime")
candy(210, -160, "cyan")
candy(360, -170, "yellow")

def firework(x, y, size, color):

    t.penup()
    t.goto(x, y)

    t.color(color)
    t.pensize(2)

    for i in range(24):

        t.penup()
        t.goto(x, y)

        t.setheading(i * 15)

        t.pendown()
        t.forward(size)

        t.backward(size * 0.25)

        t.dot(6, color)

    t.pensize(1)

firework_colors = [
    "red",
    "orange",
    "yellow",
    "lime",
    "cyan",
    "blue",
    "purple",
    "magenta",
    "white"
]

fireworks = [
    (-330, 260, 55),
    (-120, 310, 45),
    (120, 280, 60),
    (330, 240, 50)
]

for x, y, size in fireworks:

    firework(
        x,
        y,
        size,
        random.choice(firework_colors)
    )

def sparkle(x, y, color):

    t.penup()
    t.goto(x, y)

    t.dot(4, color)

for i in range(120):

    sparkle(

        random.randint(-470,470),

        random.randint(120,340),

        random.choice(firework_colors)
    )



turtle.done()