from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.pencolor("black")
        self.speed("fastest")
        self.penup()
        self.write_score(1)

    def write_score(self, score):
        self.clear()
        self.goto(-220, 250)
        self.pendown()
        message = f"Level: {score}"
        self.write(message, False, align="center", font=FONT)
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)


