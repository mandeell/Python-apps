import random
import turtle as t


def draw_square(square_size):
    for _ in range(4):
        timmy.forward(square_size)
        timmy.left(90)
def dotted_line(length,distance_up, distance_down):
    for _ in range(length):
        timmy.forward(distance_down)
        timmy.penup()
        timmy.forward(distance_up)
        timmy.pendown()
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        timmy.forward(100)
        timmy.right(angle)
def move_to_left_edge(turtle, y=None):
    """Moves the turtle to the extreme left of the screen at the current or specified y-coordinate."""
    turtle.hideturtle()
    turtle.penup()
    screen = turtle.getscreen()
    left_x = -screen.window_width() // 2
    turtle.goto(left_x, y)
    turtle.pendown()
    turtle.showturtle()
def random_walk(turtle, steps = 100, distance = 20):
    """Performs a random walk with random directions and colors."""
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        turtle.pencolor(random_color())
        turtle.setheading(random.choice(directions))
        turtle.forward(distance)

def draw_spirograph(size_of_gap):

    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(200)
        timmy.setheading(timmy.heading() + size_of_gap)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

timmy = t.Turtle()
my_screen = t.Screen()
t.colormode(255)
# my_screen.bgcolor("beige")
timmy.pensize(2)
timmy.shape("turtle")
timmy.shapesize(1)
timmy.speed(40)



draw_spirograph(2)
# print(timmy.heading())

# while my_screen:
#     random_walk(turtle=timmy, steps = 10, distance=50)




# for shape_side_n in range(2,11):
#     timmy.pencolor(random_color())
#     draw_shape(shape_side_n)












my_screen.exitonclick()
