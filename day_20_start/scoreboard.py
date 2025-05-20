from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.game_over_active = False
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=440)
        self.update_scoreboard()


    def update_scoreboard(self):
        """Displays the current score"""
        self.clear()
        self.write(f"Score: {self.score}     High score: {self.high_score}", align="center", font=("Arial", 14, "normal"))

    # method to check for collision with food and increment score by 1 each time
    def check_collision(self, snake, food):
        """Check if snake's head collides with food; if so, increments score and refreshes food"""
        # Get food's shapesize (returns tuple
        food_size = food.shapesize()
        # Calculate food's effective width in pixels (default turtle size is 20x20, scaled by stretch_wid)
        food_width = 20 * food_size[1]
        # Collision threshold: food width + buffer for snake's size
        collision_threshold = food_width * 1    # Adjust multiplier as needed

        if snake.head.distance(food) < collision_threshold:
            self.score += 1
            food.refresh()
            snake.extend()
            self.update_scoreboard()

    def game_over(self):
        """Displays the game-over message with the final score."""
        self.clear()
        self.goto(x=0, y=0)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w")as data:
                data.write(f"{self.high_score}")
            self.write(
                f"\n\nGame Over!!! \n\nScore: {self.score}.\n\nNew High score: {self.high_score}."
                f"\n\nPress R to restart game.\n\nPress Q to end the game.", align="center",
                font=("Arial", 14, "normal"))
        else:
            self.write(f"\n\nGame Over!!! \n\nScore: {self.score}.\n\nHigh score: {self.high_score}."
                       f"\n\nPress R to restart game.\n\nPress Q to end the game.", align="center",
                       font=("Arial", 14, "normal"))
        self.game_over_active = True


    def reset(self):
        """Resets the score and updates the display."""
        self.score = 0
        self.game_over_active = False
        self.goto(x=0, y=440)
        self.update_scoreboard()