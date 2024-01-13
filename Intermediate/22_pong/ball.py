import random
from turtle import Turtle

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__() 
        self.shape('circle')
        self.penup()
        self.color('white')
        self.set_random_head()

    def set_random_head(self):
        """Get random move side and angle."""
        bot_side = random.choice(range(-35, 36))
        if bot_side < 0:
            bot_side = 360 - bot_side
        gamer_side = random.choice(range(145, 216))
        self.setheading(random.choice([bot_side, gamer_side]))
    
    def move(self):
        """Move the ball."""
        self.forward(20)
        self.reflect_from_wall()
        self.check_out_of_bounds()
    
    def reflect_from_wall(self):
        """Detect collision and reflect with walls."""    
        if self.ycor() >= 245 or self.ycor() <=-270:
            self.setheading(-self.heading())
    
    def reflect_from_paddle(self):
        """Reflect from paddles."""
        self.setheading(180-self.heading())
        
    def check_out_of_bounds(self):    
        """Detect out of bounds."""
        if self.xcor() > 400 or self.xcor() < -415:
            self.goto(0, 0)
            self.set_random_head()
