from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.pencolor("white")
        self.speed("fastest")
        self.penup()
        self.write_score(0)

    def write_score(self, score):
        self.clear()
        self.goto(0, 270)
        self.pendown()
        with open("highscore.txt", mode="r") as file:
            high_score = int(file.read())
            file.close()
        if score > high_score:
            with open("highscore.txt", mode="w") as file:
                file.write(f"{score}")
                file.close()
            high_score = score
        message = f"Score: {score} HighScore: {high_score}"
        self.write(message, False, align="center", font=("Arial", 20, "normal"))
        self.penup()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 25, "normal"))
