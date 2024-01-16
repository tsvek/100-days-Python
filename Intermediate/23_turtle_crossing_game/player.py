from turtle import Turtle

class Player(Turtle):

    def __init__(self, shape: str = "turtle") -> None:
        super().__init__(shape)
        self.penup()
        self.setheading(90)
        self.goto(0, -270)

    def move_up(self):
        self.forward(20)

    def reset_position(self):
        self.goto(0, -270)