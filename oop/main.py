from turtle import Turtle, Screen
from prettytable import PrettyTable

my_table = PrettyTable()
my_table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
my_table.add_rows(
    [
["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
# print(my_table)

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

