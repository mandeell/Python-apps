import random
import turtle

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=2                                     )
        self.color("blue")
        self.speed("fastest")
        self.random_x = random.randint(-480, 480)
        self.random_y = random.randint(-480, 480)
        self.goto(x=self.random_x, y=self.random_y)

    def refresh(self):
        """Moves the food to a new random position on a 20x20 grid."""
        random_x = random.randint(-480, 480)   # -480 to 480 in 20-pixel steps
        random_y = random.randint(-480, 480)
        self.goto(x=random_x, y=random_y)