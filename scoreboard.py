
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.high_scores = 0
        self.penup()
        self.color('white')
        self.goto(0, 265)
        self.hideturtle()
        self.write_scores()

    def write_scores(self):
        self.clear()
        self.write(f'Scores : {self.scores} High Scores {self.high_scores}', align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.scores > self.high_scores:
            self.high_scores = self.scores
        self.scores = 0
        self.write_scores()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def increment_scores(self):
        self.scores += 1
        self.write_scores()



