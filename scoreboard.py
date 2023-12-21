from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)