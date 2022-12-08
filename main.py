from turtle import Turtle, Screen
import random

pointer = Turtle()
screen = Screen()

# pointer.pd()
# pointer.speed("fastest")

# def move_forwards():
#     pointer.forward(10)

# def move_backwards():
#     pointer.backward(10)

# def turn_clockwise():
#     new_heading = pointer.heading() - 10
#     pointer.setheading(new_heading)
#     pointer.forward(10)

# def turn_counter_clockwise():
#     new_heading = pointer.heading() + 10
#     pointer.setheading(new_heading)
#     pointer.forward(10)

# def clear():
#     pointer.clear()
#     pointer.pu()
#     pointer.home()
#     pointer.pd()


# screen.listen()
# screen.onkey(key = "w", fun = move_forwards)
# screen.onkey(key = "s", fun = move_backwards)
# screen.onkey(key = "a", fun = turn_counter_clockwise)
# screen.onkey(key = "d", fun = turn_clockwise)
# screen.onkey(key = "c", fun = clear)
# screen.exitonclick()



screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "blue", "yellow", "green", "orange", "purple"]
y_positions = [100, 60, 20, -20, -60, -100]

for i in range (len(colors)):
    turtle = Turtle("turtle")
    turtle.pu()
    turtle.goto(x = -210, y = y_positions[i])
    turtle.color(colors[i])









screen.exitonclick()


