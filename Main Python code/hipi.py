import turtle
import math
from turtle import *
import cmath
import time

#now we will make a graph that shows that pi is irrational

screen = turtle.Screen()
#initialize the screen

bgcolor("black")
#so we can actually see the drawing

pen = turtle.Turtle()
#we are making a turtle object called pen

pen.hideturtle()
#we are hiding the turtle so we can just see the drawing

pen.color("white")
#set the pen color to white

pen.speed(0)
#initialize the speed of the pen to the fastest

pen.pensize(2)
#initialize the pen size to 2

#now the main part of the code
#ig the math

def z(theta):
    return cmath.exp(1j * theta) + cmath.exp(1j * theta * math.pi)

# 1j means the imaginary unit in complex numbers, representing the square root of -1

pen.penup()

theta = 0 
#starting angle

step = 0.01
#how much we increase theta by in each iteration


scale = 120
#scaling factor to make the graph fit well on the screen, so that it is not too small or too big

start = z(theta)
pen.goto(start.real * scale, start.imag * scale)
pen.pendown()

while True:
    theta += step
    point = z(theta)
    x = point.real * scale
    y = point.imag * scale

    pen.goto(x, y)

