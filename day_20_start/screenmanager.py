from turtle import Screen
from snake import Snake
import time
from scoreboard import Scoreboard
from food import Food

class ScreenManager():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1000, height=1000)
        self.screen.getcanvas().winfo_toplevel().resizable(width=False, height=False)
        self.screen.title("My snake game")
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        self.snake = Snake()
        self.scoreboard = Scoreboard()
        self.food  = Food()

        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.snake.up)
        self.screen.onkey(key="Down", fun=self.snake.down)
        self.screen.onkey(key="Left", fun=self.snake.left)
        self.screen.onkey(key="Right", fun=self.snake.right)

    def run_game(self):
        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.2)
            self.snake.move()
            self.scoreboard.check_collision(self.snake, self.food)

            if abs(self.snake.head.xcor()) > 500 or abs(self.snake.head.ycor()) > 500:
                game_is_on = False
        self.screen.exitonclick()