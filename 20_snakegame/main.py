from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from helpers import create_move_function
import time

GAME_SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ouroboros")

snake = Snake(screen=screen)
food = Food()
scoreboard = ScoreBoard()

game_on = True


def detect_collision(snake, food, scoreboard):
    if food.distance(snake.head) < 10:
        food.spawn()
        snake.grow()
        scoreboard.update_score()


while game_on:
    screen.update()
    time.sleep(GAME_SPEED)
    snake.move()
    detect_collision(snake, food, scoreboard)
    if snake.detect_collision_with_wall() or snake.detect_collision_with_tail():
        game_on = False
        screen.title("Game Over!")
        scoreboard.write_game_over()


screen.exitonclick()

