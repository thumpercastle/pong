from turtle import Turtle
import random

STARTHEADING = random.randint(5, 60)
SPEED = 1

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setpos(position)
        self.setheading(STARTHEADING)
        self.move_speed = 0.1

    def move_forward(self):
        self.speed(SPEED)
        self.forward(10)

    def bounce_y(self):
        if self.ycor() > 280:
            self.setheading(360 - self.heading())
        elif self.ycor() < -280:
            self.setheading(360 - self.heading())

    def bounce_x(self):
        self.setheading(180 - self.heading())
        self.move_speed *= 0.9

    def out_of_bounds(self, direction):
        self.setpos(0, 0)
        self.setheading(direction)
