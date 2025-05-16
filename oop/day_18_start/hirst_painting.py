import random
import turtle as t


def hirst_dot_painting(turtle,length,space_between_dot,height):
    for _ in range(height):
        dotted_line(length-1, space_between_dot)
        turtle.setheading(90)
        turtle.dot(50, (random_color()))
        turtle.penup()
        turtle.forward(100)
        turtle.setheading(180)
        dotted_line(length-1, space_between_dot)
        turtle.setheading(90)
        turtle.dot(50, (random_color()))
        turtle.penup()
        turtle.forward(100)
        turtle.setheading(0)
        # timmy.setheading(90)
        # dotted_line(1,100)
def start_at_the_left_side(turtle):
    turtle.setheading(180)
    turtle.penup()
    turtle.forward(600)
    turtle.setheading(270)
    turtle.forward(550)
    turtle.setheading(0)
def dotted_line(length,distance_up):
    for _ in range(length):
        timmy.dot(50,(random_color()))
        timmy.penup()
        timmy.forward(distance_up)
        timmy.pendown()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

# color_list = [(199, 176, 117), (124, 37, 24), (166, 106, 57), (6, 57, 83), (185, 158, 54), (108, 68, 84)]
timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)
timmy.speed(40)
timmy.hideturtle()



start_at_the_left_side(timmy)
hirst_dot_painting(timmy,10,100,5)




screen.exitonclick()