from player import Player
from scoreboard import ScoreBoard
from turtle import Screen, Turtle
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True

while game_on:
    sleep(0.1)
    screen.update()

    scoreboard.show_level()

    if player.ycor() > 270:
        scoreboard.level_up()
        player.reset_position()

screen.exitonclick()
