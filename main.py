from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_forward()
    ball.bounce_y()
    # Paddle bounce
    if ball.xcor() > 320 and (r_paddle.ycor() - 50) < ball.ycor() < (r_paddle.ycor() + 50) or ball.xcor() < -320 and \
            (l_paddle.ycor() - 50) < ball.ycor() < (l_paddle.ycor() + 50):
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.out_of_bounds(random.randint(120, 175))
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    elif ball.xcor() < -370:
        ball.out_of_bounds(random.randint(5, 60))
        scoreboard.r_point()
        scoreboard.update_scoreboard()


screen.exitonclick()

# Court
