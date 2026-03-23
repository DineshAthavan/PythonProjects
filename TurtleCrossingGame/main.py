import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = []
level = 1

for num_cars in range(0, 30):
    cars.append(CarManager(random.randint(-340, 340), random.randint(-250, 250)))
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        if car.distance(player) <= 25:
            scoreboard.game_over()
            game_is_on = False
            break
        else:
            car.drive_fwd()
    if player.is_finished():
        level += 1
        scoreboard.write_score(level)
        for car in cars:
            car.update_move_dist()


screen.exitonclick()
