from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.resizemode("user")
        self.shapesize(stretch_len=2)
        self.penup()
        self.setpos(x, y)
        self.seth(180)
        self.move_size = STARTING_MOVE_DISTANCE

    def drive_fwd(self):
        if self.xcor() >= -340:
            self.forward(self.move_size)
        else:
            self.goto(350, self.ycor())
            self.forward(self.move_size)

    def update_move_dist(self):
        self.move_size += MOVE_INCREMENT

