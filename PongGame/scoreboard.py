from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.ht()
        self.pencolor("white")
        self.speed("fastest")
        self.penup()
        self.x = x
        self.y = y
        self.write_score(0)

    def write_score(self, score):
        self.clear()
        self.goto(self.x, self.y)
        self.pendown()
        message = f"Score: {score}"
        self.write(message, False, align="center", font=("Arial", 15, "normal"))
        self.penup()
