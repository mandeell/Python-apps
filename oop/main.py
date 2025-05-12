from turtle import Turtle, Screen
from prettytable import PrettyTable

my_table = PrettyTable()
# my_table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

my_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
my_table.add_column("Type", ["Electric", "Water", "Fire"])
my_table.align = "r"
print(my_table.align)
print(my_table)

# shadow = Turtle()
# shadow_screen = Screen()
# print(shadow_screen.canvheight,shadow.screen,shadow_screen.title("Welcome to my Game!!"))
# print(shadow_screen.bgcolor("beige"))
# shadow.shape("turtle")
# shadow.shapesize(2)
# shadow.color('coral')
#
# shadow.penup()
# shadow.goto(-200, 150)  # Start position (top-left of table)
# table_lines = my_table.get_string().split('\n')
# for line in table_lines:
#     shadow.write(line, align="left", font=("Courier", 10, "normal"))
#     shadow.sety(shadow.ycor() - 20)  # Move down for next line
#
# # Turtle movements
# shadow.pendown()
# shadow.left(300)
# shadow.forward(250)
#
# shadow_screen.exitonclick()

