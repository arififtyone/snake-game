from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 20, "normal"))


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 20, "normal"))
