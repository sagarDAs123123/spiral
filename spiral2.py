import turtle
t=turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")

for i in range(200):
    t.color("red")
    t.circle(i)
    t.left(5)
turtle.done()
