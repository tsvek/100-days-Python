import time

from food import Food
from scoreboard import Score
from snake import Snake
from turtle import Screen
# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snale_game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Score()
# Control 
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
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.grow()
        score.point()
        if score.score % 5 == 0:
            game_speed -= 0.01
    # Detect collision with walls and tail
    vertical_wall = snake.head.xcor() < -299 or snake.head.xcor() > 280
    horizontal_wall = snake.head.ycor() < -280 or snake.head.ycor() > 260
    tail_collision = snake.tail_collision()
    if vertical_wall or horizontal_wall or tail_collision:
        score.game_over()
        game_on = False

screen.exitonclick()