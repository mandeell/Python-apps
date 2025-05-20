from turtle import Screen
from snake import Snake
import time
from scoreboard import Scoreboard
from food import Food

class ScreenManager:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1000, height=1000)
        self.screen.getcanvas().winfo_toplevel().resizable(width=False, height=False)
        self.screen.title("My snake game")
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.screen.reset_game = self.reset_game


        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.snake.up)
        self.screen.onkey(key="Down", fun=self.snake.down)
        self.screen.onkey(key="Left", fun=self.snake.left)
        self.screen.onkey(key="Right", fun=self.snake.right)
        self.screen.onkey(key="r", fun=self.reset_game)
        self.screen.onkey(key="q", fun=self.end_game)

    def run_game(self):
        game_is_on = True
        while game_is_on:
            if not self.scoreboard.game_over_active: # Only update if not in game-over state
                self.screen.update()
                time.sleep(0.2)
                self.snake.move()

            # detect collision with food
                self.scoreboard.check_collision(self.snake, self.food)

            # detect collision with wall
                if (abs(self.snake.head.xcor()) > 480 or abs(self.snake.head.ycor()) > 480 or
                        self.snake.check_self_collision()):
                    self.scoreboard.game_over()
            self.screen.update()
            time.sleep(0.1)




        self.screen.exitonclick()

    def reset_game(self):
        self.scoreboard.reset()
        self.snake.reset()
        self.food.refresh()

    def end_game(self):
        self.screen.bye()