import random
from turtle import Turtle,Screen


my_screen = Screen()
my_screen.setup(width=1000, height=800)
my_screen.title("Turtle Race")
is_race_on = False
user_bet = my_screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-250, -150, -50, 50, 150, 250]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-480, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 480:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won!!!, The {winning_color.upper()} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color.upper()} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

my_screen.exitonclick()

