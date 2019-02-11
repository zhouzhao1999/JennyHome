#My first python picture for a house

import turtle
import time

my = turtle.Turtle()
my.hideturtle()
turtle.colormode(255)
my.speed(10)

turtle.setup(1200, 800, 0, 0)


# 画线
def line(ttl, fromx, fromy, tox, toy):
    ttl.penup()
    ttl.goto(fromx, fromy)
    ttl.pendown()
    ttl.goto(tox, toy)

# 画梯形
def trapezoidal(x,y,direction,addheight):
    p=0
    r=0
    if direction=='left':
        p=0
        r=41.25
    if direction == 'right':
        p=41.25
        r=0
    line(my, -45-x, p-y, 45-x, r-y)
    line(my, 45-x, r-y, 45-x, -41.25-addheight-y)
    line(my, 45-x, -41.25-addheight-y, -45-x, -41.25-addheight-y)
    line(my, -45-x, -41.25-addheight-y, -45-x, p-y)

# 画长方形
def rectangle(x, y):
    line(my, -45 - x, 77.5 - y, 45 - x, 77.5 - y)
    line(my, 45 - x, 77.5 - y, 45 - x, -77.5 - y)
    line(my, 45 - x, -77.5 - y, -45 - x, -77.5 - y)
    line(my, -45 - x, -77.5 - y, -45 - x, 77.5 - y)

# 写字
def labelPoint(ttl, x, y, label):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.write(label, font=("Arial", 37, "normal"))
    ttl.penup()


# 轮廓#
line(my, 0, 210, 235, 75)
line(my, 235, 75, 235, -245)
line(my, 235, -245, -235, -245)
line(my, -235, -245, -235, 75)
line(my, -235, 75, 0, 210)

trapezoidal(52,-100,'left',50)
trapezoidal(156,-50,'left',0)
trapezoidal(-52,-100,'right',50)
trapezoidal(-156,-50,'right',0)


rectangle(52, 100)
rectangle(156, 100)
rectangle(-52, 100)
rectangle(-156, 100)

line(my, -235, -200, 235, -200)
labelPoint(my, -60, -250, "Aladdin")

##屋顶


my.color("#66c6f5")
my.begin_fill()

my.penup()
my.goto(-235,75)
my.pendown()
my.left(135)
my.forward(20)
my.right(112)
my.forward(41.4)

for _ in range(5):
    my.left(45)
    my.forward(10)
    my.right(45.2)
    my.forward(41.4)

my.right(45)
my.forward(41.4)

for _ in range(5):
    my.right(45)
    my.forward(10)
    my.left(45.2)
    my.forward(41.4)
my.goto(235,75)
my.goto(0,210)
my.goto(-235, 75)

my.end_fill()

time.sleep(100)

