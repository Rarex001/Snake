import turtle

from turtle import Turtle
import random

class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 255)
        self.write(f"Score: {score}", align="center", font=("Courier", 16, "bold"))

    def game_over(self):
        self.goto(10, 0)
        self.write(f"GAME OVER!", align="center", font=("Courier", 20, "bold"))
