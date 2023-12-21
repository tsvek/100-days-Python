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
            self.grow()


    def grow(self):
        """Add segment after cath the food."""
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        if len(self.body) == 0:
            segment.goto(0, 0)
        else:
            segment.goto(self.body[-1].xcor(), self.body[-1].ycor())
        self.body.append(segment)

    def move(self):
        """Moving snake."""
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def tail_collision(self):
        for segment in self.body[1:]:
            if self.head.distance(segment) < 10:
                return True



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)