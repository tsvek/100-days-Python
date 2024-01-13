from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position) -> tuple:
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.derection = 1

    def up(self):
        """Move up."""
        if self.ycor() < 210:
            self.forward(40)

    def down(self):
        """Move down."""
        if self.ycor() > -240:
            self.forward(-40)
   
    def move(self):
        """Move bot paddle."""
        if self.ycor() == 210 or self.ycor() == -240:
            self.derection *= -1
        self.forward(10 * self.derection)
            
