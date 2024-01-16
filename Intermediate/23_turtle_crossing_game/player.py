from turtle import Turtle

START = (0, -280)
MOVE_DISTANCE = 20
FINISH = (0, 288)

class Player(Turtle):

    def __init__(self, shape: str = "turtle") -> None:
        super().__init__(shape)
        self.penup()
        self.setheading(90)
        self.goto(START)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(START)