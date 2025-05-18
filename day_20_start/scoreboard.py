import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=440)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Displays the current score"""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))



    def check_collision(self, snake, food):
        """Check if snake's head collides with food; if so, increments score and refreshes food"""
        if snake.head.distance(food) < 15:
            self.score += 1
            food.refresh()
            snake.extend()
            self.update_scoreboard()