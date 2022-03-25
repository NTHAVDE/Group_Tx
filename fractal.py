from turtle import *
from random import *
import turtle
speed(0)
turtle.tracer(0,0)
#grass
bgcolor("green")


penup()
goto(-400, -100)
pendown()
#sky
color("skyblue")
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()

# Sun
penup()
goto(-320, 225)
pendown()
color("yellow")
begin_fill()
circle(35)
end_fill()

# Cloud
penup()
goto(200, 200)
pendown()
color("white")
begin_fill()
circle(25)
end_fill()

penup()
goto(220, 240)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(230, 215)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(180, 225)
pendown()
begin_fill()
circle(25)
end_fill()
penup()




t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()

x = -100
turtles = [t1,t2,t3,t4,t5]
for t in turtles:
  t.speed(100)
  t.left(90)
  t.color('brown')
  t.pu()
  x += randint(80,160)
  t.goto(x, randint(-100,-100))
  t.pd()


def branch(turt, len_branch):
  angle = randint(22,30)
  sf = uniform(0.6,0.8)
  size = int(len_branch /10)
  turt.pensize(size)
  if len_branch < 20:
    turt.color('green')
    turt.stamp()
    turt.color('brown')

  if len_branch > 10:
    turt.forward(len_branch)
    turt.left(angle)
    branch(turt, len_branch*0.7)
    turt.right(angle*2)
    branch(turt, len_branch*0.7)
    turt.left(angle)
    turt.backward(len_branch)

for t in turtles:
  branch(t,100)

turtle.done()
