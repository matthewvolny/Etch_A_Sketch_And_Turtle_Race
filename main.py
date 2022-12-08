from turtle import Turtle, Screen
import random

# pointer = Turtle()
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

race_on = False
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "blue", "yellow", "green", "orange", "purple"]
y_positions = [105, 65, 25, -15, -55, -95]
turtle_list = []


for i in range (0, 6):
    turtle = Turtle("turtle")
    turtle.color(colors[i])
    turtle.pu()
    turtle.goto(x = -210, y = y_positions[i])
    turtle_list.append(turtle)
    
if user_bet:
    race_on = True

while race_on:
    rand_int = random.randint(0, 10)
    rand_turtle = random.choice(turtle_list)
    rand_turtle.forward(rand_int)
    if rand_turtle.xcor() > 230:
        race_on = False
        winning_color = rand_turtle.pencolor()
        if winning_color == user_bet:   
            print(f"You won!. The {rand_turtle.pencolor()} turtle finished first.")
        else:
            print(f"You lost. The {rand_turtle.pencolor()} turtle finished first.")

screen.exitonclick()


