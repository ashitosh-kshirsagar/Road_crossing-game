from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highest_level.txt") as highest_level_score:
            highest_level = int(highest_level_score.read())
        self.highest_level = highest_level
        self.level = 0
        self.hideturtle()
        self.goto(-480, 300)
        self.color("white")
        self.write(arg=f"LEVEL: {self.level} \nHIGHEST LEVEL: {self.highest_level}", align="left",
                   font=("Arial", 15, "normal"))

    def update_score(self):
        self.level += 1
        if self.level > self.highest_level:
            self.highest_level = self.level
        self.clear()
        self.write(arg=f"LEVEL: {self.level} \nHIGHEST LEVEL: {self.highest_level} ", align="left",
                   font=("Arial", 15, "normal"))

        with open("highest_level.txt", mode="w") as highest_level_score:
            highest_level_score.write(f"{self.highest_level}")

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(arg="GAME OVER ", align="center", font=("Arial", 30, "normal"))