from turtle import Turtle
import random
import wall

AVAILABLE_POSITION = [300, 280, 260, 240, 220, 200, 180, 160, 140, 120, 100, 80, 60, 40, 20, 0, -20, -40,
                       -60, -80, -100, -120, -140, -160, -180, -200, -220, -240, -260, -280, -300]
POSITION_WALL = []
POSITION_SNAKE = []

class Food(Turtle):
    def __init__(self, level):
        self.level = level
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def position_snake(self, position):
        POSITION_SNAKE.extend(position)

    def refresh(self):
        if self.level == "Medium":
            POSITION_WALL.extend(wall.POSITION_MEDIUM)
        elif self.level == "Easy" or self.level == "Hard":
            POSITION_WALL.extend(wall.POSITION_NON_FOOD)
        while True:
            random_x_y = (random.choice(AVAILABLE_POSITION), random.choice(AVAILABLE_POSITION))
            if random_x_y not in POSITION_WALL and random_x_y not in POSITION_SNAKE:
                self.goto(random_x_y)
                POSITION_SNAKE.clear()
                return