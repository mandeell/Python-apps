from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Module-level constant for initial snake positions
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, color = "white", head_shape = "square"):
        self.segments = []
        self.color = color
        self.head_shape = head_shape
        self.create_snake()
        self.head = self.segments[0]  # Head is the first segment

    def check_self_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def create_snake(self):
        """Creates the initial snake with segments at starting positions."""
        for index, position in enumerate(STARTING_POSITIONS):
            new_segment = Turtle("square" if index > 0 else self.head_shape)
            new_segment.color(self.color)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Moves the snake forward, each segment following the previous one."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color(self.color)
        new_segment.penup()
        last_segment = self.segments[-1]
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(new_segment)

    def reset(self):
        """Clears the current snake and recreates it at starting positions."""
        for segment in self.segments:
            segment.hideturtle()  # Hide segments to remove from screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        """Turns the snake up if not already heading down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turns the snake down if not already heading up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turns the snake left if not already heading right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turns the snake right if not already heading left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

