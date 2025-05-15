# import colorgram
#
# rgb_color = []
# color_pallete = colorgram.extract('image.jpg', 10)
# for color in color_pallete:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
# print(rgb_color)

import random
import turtle as t



def dotted_line(length,distance_up):
    for _ in range(length):
        timmy.dot(50,random.choice(color_list))
        timmy.penup()
        timmy.forward(distance_up)
        timmy.pendown()
def random_color():
    my_color = random.choice(color_list)
    return my_color
def move_to_left_edge(turtle, y=None):
    """Moves the turtle to the extreme left of the screen at the current or specified y-coordinate."""
    turtle.hideturtle()
    turtle.penup()
    my_screen = turtle.getscreen()
    left_x = -my_screen.window_width() // 2
    turtle.goto(left_x, y)
    turtle.pendown()
    turtle.showturtle()

color_list = [(199, 176, 117), (124, 37, 24), (166, 106, 57), (6, 57, 83), (185, 158, 54), (108, 68, 84)]
timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)


timmy.shape("turtle")
timmy.shapesize(1)
timmy.speed(40)
move_to_left_edge(timmy)
timmy.dot(50,random.choice(color_list))
dotted_line(10,100)






screen.exitonclick()