from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)
score_1 = ScoreBoard(200, 280)
score_2 = ScoreBoard(-200, 280)
ball = Ball()
score_paddle_1 = 0
score_paddle_2 = 0

screen.listen()
screen.onkeypress(paddle_1.paddle_up, "Up")
screen.onkeypress(paddle_1.paddle_down, "Down")
screen.onkeypress(paddle_2.paddle_up, "w")
screen.onkeypress(paddle_2.paddle_down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detecting collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        # Increasing the speed of ball. Can be also done by decreasing sleep time.
        if abs(ball.x_move) < 20:
            ball.x_move *= 1.05
            ball.y_move *= 1.05
        ball.bounce_x()

    # Detecting miss of ball by paddle_1
    if ball.xcor() > 380:
        ball.ball_reset()
        # Reset ball speed before score update
        ball.x_move = 10
        ball.y_move = 10
        score_paddle_2 += 1
        score_2.write_score(score_paddle_2)

    # Detecting miss of ball by paddle_2
    if ball.xcor() < -380:
        ball.ball_reset()
        # Reset ball speed before score update
        ball.x_move = 10
        ball.y_move = 10
        score_paddle_1 += 1
        score_1.write_score(score_paddle_1)

screen.exitonclick()
