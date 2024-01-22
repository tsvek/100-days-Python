import random

from turtle import Turtle

COLORS = ['red', 'yellow', 'blue', 'green', 'purple']
START_MOVE = 5

class CarManager():

    def __init__(self) -> None:
        self.all_cars = []
        self.speed = START_MOVE

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle(shape='square')
            new_car.penup()
            new_car.shapesize(stretch_len=2)
            new_car.goto(300, random.randint(-240, 240))
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)
            if car.xcor() < -330:
                car.clear()
                car.hideturtle()

    def speed_increase(self):
        self.speed += 1