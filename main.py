import time
import turtle
import random
from food import Food
from snake import Snake
from scoreboard import Scoreboard


screen = turtle.Screen()

def screen_init():
    screen.setup(width = 600,height = 600)
    screen.tracer(0)
    screen.bgcolor("black")
    screen.title("Snake")


score = 0
screen_init()
snake = Snake()
food = Food()
scoreboard = Scoreboard(score)
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move(20)

    if snake.head.distance(food) < 15: # food collisoion
        score += 1
        food.goto(1000, 1000)
        scoreboard.goto(1000, 1000)
        scoreboard.clear()
        food = Food()
        scoreboard = Scoreboard(score)
        snake.extend()

    # wall collision
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # intself collision
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 5:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()
