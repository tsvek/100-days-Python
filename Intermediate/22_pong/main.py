import time

from ball import Ball
from paddle import Paddle
from playing_field import Field
from scoreboard import Score
from turtle import Screen

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong!")
screen.tracer(0)

field = Field()

user = Paddle((-355, 0))
bot = Paddle((350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(user.up, "Up")
screen.onkey(user.down, "Down")

game_on = True
field

while game_on:
    screen.update()
    time.sleep(0.1)
    
    bot.move()
    ball.move()

    # Paddle collision
    if (bot.distance(ball) < 50 and ball.xcor() > 330) or (user.distance(ball) < 50 and ball.xcor() < -335):
        ball.reflect_from_paddle()
    
    # Out of bound and points
    if ball.xcor() > 400: 
        ball.out_of_bounds()
        score.user_point()
    elif ball.xcor() < -415:
        ball.out_of_bounds()
        score.bot_point()


screen.exitonclick()