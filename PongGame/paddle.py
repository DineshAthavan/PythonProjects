from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setpos((x, y))
        self.seth(90)

    def paddle_up(self):
        self.forward(20)

    def paddle_down(self):
        self.backward(20)



