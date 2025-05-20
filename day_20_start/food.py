import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=2                                     )
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Moves the food to a new random position on a 20x20 grid."""
        random_x = random.randint(-24, 24)  * 20  # -480 to 480 in 20-pixel steps
        random_y = random.randint(-24, 24) * 20
        self.goto(x=random_x, y=random_y)