import turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    blocks = []

    def __init__(self):
        self.create_block(0, 0)
        self.create_block(-20, 0)
        self.create_block(-40, 0)
        self.head = self.blocks[0]
        
    def create_block(self, x, y):
        tim = turtle.Turtle("square")
        tim.penup()
        tim.color("white")
        tim.goto(x, y)
        self.blocks.append(tim)

    def extend(self):
        self.create_block(self.blocks[-1].xcor(), self.blocks[-1].ycor())

    def move(self, d):
        for i in range(len(self.blocks) - 1, 0, -1):
            x = self.blocks[i - 1].xcor()
            y = self.blocks[i - 1].ycor()
            self.blocks[i].goto(x, y)
        self.head.forward(d)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
