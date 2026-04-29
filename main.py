from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('black')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()


def move_heading(t):
    t.forward(5)

    if t.xcor() > 240 or t.xcor() < -240:
        t.setheading(180 - t.heading())
        
    if t.ycor() > 240 or t.ycor() < -240:
            t.setheading( -t.heading())

def move_xy(turtle, deltaX, deltaY):
    newX = turtle.xcor() + deltaX
    newY = turtle.ycor() + deltaY

    if newX > 240 or newX < -240:
        newX = turtle.xcor()
        deltaX *= -1
    
    if newY > 240 or newY < -240:
        newY = turtle.ycor()
        deltaY *= -1
    
    turtle.goto(newX, newY)
    return deltaX,deltaY    

class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.alive = True
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        self.forward(4)
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())




screen = Screen()
screen.bgcolor("black")
screensize(580,580)
screen.listen()

playing_area()

t = Turtle()

alive = True
p1 = Player(-100, 0, "red",screen, "d", "a")

turtles = [t]

for i in range(10):
    t = Turtle("circle")
    t.color("red")
    t.speed(0)
    t.setheading(random.randint(0, 360))
    turtles.append(t)

while alive:
    for turt in turtles:
        move_heading(turt)
    p1.move()















screen.exitonclick()