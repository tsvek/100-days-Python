from turtle import Turtle

ALIGN = 'center'
FONT = ("Arial", 20, "bold")

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 270)
        self.color("black")

    def show_level(self):
        self.write(f"Level {self.level}", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.show_level()