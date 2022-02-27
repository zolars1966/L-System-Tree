import turtle
import time
from random import randint

turtle.screensize(1280, 720)
turtle.penup()
turtle.setpos(0, -350)
turtle.left(90)
turtle.pendown()

rules = {
    "+":"+",
    "-":"-",
    "[":"[",
    "]":"]",
    "@":"@",
    "X":"F[@[-X]+X]",
    "F":"F"
}

f = "X"
def angle():
    return randint(0, 45)
# angle = 25
length = 80
stack = []

for i in range(15):
    ff = ""
    for sym in f:
        ff += rules[sym]

    f = ff

    turtle.tracer(0)

    for sym in f:
        if sym == "-":
            turtle.right(angle())
        elif sym == "+":
            turtle.left(angle())
        elif sym == "F":
            turtle.forward(length)
        elif sym == "[":
            stack.append((turtle.heading(), turtle.pos(), length))
        elif sym == "]":
            angle_, pos_, length = stack.pop()
            turtle.penup()
            turtle.setheading(angle_)
            turtle.setpos(pos_)
            turtle.pendown()
        elif sym == "@":
            length -= 6

    turtle.tracer(1)
    time.sleep(1)

    turtle.clear()
    turtle.penup()
    turtle.setpos(0, -350)
    turtle.pendown()

print(f)

for sym in f:
    if sym == "-":
        turtle.right(angle())
    elif sym == "+":
        turtle.left(angle())
    elif sym == "F":
        turtle.forward(length)
    elif sym == "[":
        stack.append((turtle.heading(), turtle.pos(), length))
    elif sym == "]":
        angle_, pos_, length = stack.pop()
        turtle.penup()
        turtle.setheading(angle_)
        turtle.setpos(pos_)
        turtle.pendown()
    elif sym == "@":
        length -= 6

turtle.exitonclick()
