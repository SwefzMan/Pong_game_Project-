from turtle import Turtle, Screen
from  paddle import Paddle
from ball import Ball
from scoreborad import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreborad = ScoreBoard()
self = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on :
    time.sleep(0.055)
    screen.update()
    ball.move()

#     detect collipes with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#     detect collipes with the paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 300 or ball.distance(l_paddle) < 30 and ball.xcor() < -300  :
        ball.bounce_x()

#     detect when miss ball
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreborad.l_point()

    if ball.xcor() < -380 :
        ball.reset_position()
        scoreborad.r_point()

screen.exitonclick()