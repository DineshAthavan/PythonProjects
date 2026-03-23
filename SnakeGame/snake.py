from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.seg = []
        self.snake_create()
        self.head = self.seg[0]

    def snake_create(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.seg.append(new_seg)

    def extend_snake(self):
        self.add_snake(self.seg[-1].position())

    def snake_move(self):
        for i in range(len(self.seg) - 1, 0, -1):
            new_x = self.seg[i - 1].xcor()
            new_y = self.seg[i - 1].ycor()
            self.seg[i].goto(new_x, new_y)
        self.seg[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
