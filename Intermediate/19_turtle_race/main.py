import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet!", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

start=-100
for col in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(col)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start)
    start += 30
    turtles.append(new_turtle)
game_on = False

if user_bet:
    game_on = True

while game_on:
    for tur in turtles:
        if tur.xcor() > 200:
            if user_bet.lower() == tur.pencolor().lower():
                print("You won!")
            else:    
                print(f"{tur.pencolor().capitalize()} turtle win! You lose!")
            game_on = False 
        rand_distance = random.randint(0, 10)
        rand_speed = random.randint(1, 10)
        tur.speed(rand_speed)
        tur.forward(rand_distance)

screen.exitonclick()