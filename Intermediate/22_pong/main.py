import time

from ball import Ball
from paddle import Paddle
from playing_field import Field
from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong!")
screen.tracer(0)

field = Field()

user = Paddle((-355, 0))
bot = Paddle((350, 0))
ball = Ball()
screen.listen()
screen.onkey(user.up, "Up")
screen.onkey(user.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    field
    bot.move()
    ball.move()

    if (bot.distance(ball) < 50 and ball.xcor() > 330) or (user.distance(ball) < 50 and ball.xcor() < -335):
        ball.reflect_from_paddle()


screen.exitonclick()