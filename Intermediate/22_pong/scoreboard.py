from turtle import Turtle

ALIGN = 'center'
FONT = ("Arial", 20, "bold")

class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.bot_score = 0
        self.user_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto((0, 265))
        self.show_score()

    def show_score(self):
        """Show game score."""
        self.write(f"{self.user_score}    {self.bot_score}", move=False, align=ALIGN, font=FONT)

    def bot_point(self):
        """Point for bot."""
        self.clear()
        self.bot_score += 1
        self.show_score()
    
    def user_point(self):
        """Point for user."""
        self.clear()
        self.user_score += 1
        self.show_score()
