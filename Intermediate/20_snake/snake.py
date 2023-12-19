from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):

    def __init__(self) -> None:
        self.body = []
        self.create_body()
        self.head = self.body[0]

    def create_body(self):
        """Create starting snake body."""
        for id in range(3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            if id != 0:
                segment.forward(-20*id)
            self.body.append(segment)

    def move(self):
        """Moving snake."""
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)