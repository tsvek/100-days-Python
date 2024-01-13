from turtle import Turtle

class Field(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(5)
        self.pencolor('white')
        self.walls = {
            'middle': [(0, -285), 290, 90], 
            'up': [(-390, 265), 375, 0], 
            'down': [(-390, -290), 375, 0]
            }
        self.boards()
    
    def boards(self):
        """Create playing field."""
        for wall, setup in self.walls.items():
            self.setheading(setup[2])
            self.goto(setup[0])
            while (self.ycor() <= setup[1] and wall == 'middle') or (self.xcor() <= setup[1] and wall != 'middle'):
                self.pendown()
                self.forward(20)
                self.penup()
                self.forward(20)
    
