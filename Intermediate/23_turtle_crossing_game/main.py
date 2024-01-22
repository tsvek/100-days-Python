from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
from turtle import Screen
from time import sleep


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True
count = 0
speed = 0.1

while game_on:
    sleep(speed)
    screen.update()

    scoreboard.show_level()
    car_manager.create_car()
    car_manager.move()

    # Collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_on = False

    # Level up
    if player.ycor() > 270:
        scoreboard.level_up()
        player.reset_position()
        car_manager.speed_increase()
        


screen.exitonclick()
