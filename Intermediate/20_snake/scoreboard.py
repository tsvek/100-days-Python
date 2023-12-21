from turtle import Turtle, Screen

ALIGN = 'center'
FONT = ("Arial", 20, "normal")

class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(-20, 270)
        self.color("white")
        self.show_score()

    def point(self):
        self.clear()
        self.score += 1
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)
