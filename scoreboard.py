from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.write(f"Score = {self.score}", align="center", font=("Arial", 15, "normal"))
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode='w') as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 15, "normal"))

    def update(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align="center", font=("Arial", 8, "normal"))

    def increase_score(self):
        self.score = self.score + 1
        self.update()
