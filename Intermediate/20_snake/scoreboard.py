from turtle import Turtle, Screen

class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(-20, 270)
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align='center', font=("Arial", 20, "normal"))
        #self.show_score()

    def point(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align='center', font=("Arial", 20, "normal"))


