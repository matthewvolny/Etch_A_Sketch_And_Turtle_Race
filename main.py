from turtle import Turtle, Screen
import random

pointer = Turtle()
screen = Screen()

pointer.pd()
pointer.speed("fastest")

def move_forwards():
    pointer.forward(10)

def move_backwards():
    pointer.backward(10)

def turn_clockwise():
    new_heading = pointer.heading() - 10
    pointer.setheading(new_heading)
    pointer.forward(10)

def turn_counter_clockwise():
    new_heading = pointer.heading() + 10
    pointer.setheading(new_heading)
    pointer.forward(10)

def clear():
    pointer.clear()
    pointer.pu()
    pointer.home()
    pointer.pd()


screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = turn_counter_clockwise)
screen.onkey(key = "d", fun = turn_clockwise)
screen.onkey(key = "c", fun = clear)
screen.exitonclick()


