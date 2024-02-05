import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


CAR_SPAWN_PROBABILITY = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
screen.onkey(key="Up", fun=player.move)

car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    if random.random() < CAR_SPAWN_PROBABILITY:
        car_manager.spawn_car()
    car_manager.move_cars()
    if player.check_if_reached_end():
        scoreboard.advance_level()
    if car_manager.detect_collision(player):
        game_is_on = False
        scoreboard.write_game_over()
    time.sleep(scoreboard.game_speed)
    screen.update()

screen.exitonclick()
