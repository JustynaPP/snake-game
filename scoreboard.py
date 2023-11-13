from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high:
            self.high_score = int(high.read())
        self.goto(0, 280)
        self.penup()
        self.color("white")
        self.ht()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score}. High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def adding_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def game_over_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high:
                high.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

