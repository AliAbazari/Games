from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 330)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def save_high_score(self, level):
        if level == "Easy":
            if self.score > self.high_score:
                self.high_score = self.score
                with open("easy_data.txt", "w") as data:
                    data.write(f"{self.high_score}")
        elif level == "Medium":
            if self.score > self.high_score:
                self.high_score = self.score
                with open("medium_data.txt", "w") as data:
                    data.write(f"{self.high_score}")
        else:
            if self.score > self.high_score:
                self.high_score = self.score
                with open("hard_data.txt", "w") as data:
                    data.write(f"{self.high_score}")

    def load_high_score(self, level):
        if level == "Easy":
            with open("easy_data.txt") as data:
                self.high_score = int(data.read())
        elif level == "Medium":
            with open("medium_data.txt") as data:
                self.high_score = int(data.read())
        else:
            with open("hard_data.txt") as data:
                self.high_score = int(data.read())