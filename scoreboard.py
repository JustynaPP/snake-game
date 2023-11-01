from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.penup()
        self.color("white")
        self.ht()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def adding_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
