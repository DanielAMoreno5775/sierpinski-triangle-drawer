import turtle
import sys

#turtle setup
#sys.setExecutionLimit(999999999999999) #So that page doesn't time out during drawing

turtle.speed(0)

def triangle(side):
    turtle.setheading(180)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)

def Sierpinski(depth, length):
    if depth == 1:
        triangle(length)
    else:
        Sierpinski(depth - 1, length)
        turtle.right(120)
        turtle.forward(length * 2 ** (depth - 2))
        Sierpinski(depth - 1, length)
        turtle.left(120)
        turtle.forward(length * 2 ** (depth - 2))
        Sierpinski(depth - 1, length)
        turtle.forward(length * 2 ** (depth - 2))
        
turtle.penup()
turtle.setx(-180)
turtle.sety(-180)
turtle.pendown()

#min length of 8
#layer 6 creates 9 recursion triangles
Sierpinski(6, 8)
turtle.Screen().exitonclick() #prevents window from closing the moment the program ends