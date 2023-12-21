import time

from food import Food
from scoreboard import Score
from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snale_game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
game_speed = 0.2

while game_on:
    screen.update()
    time.sleep(game_speed)

    snake.move()

    if snake.head.distance(food) < 15:
        food.new_food()
        snake.grow()
        score.point()


screen.exitonclick()