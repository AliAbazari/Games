from turtle import Turtle

POSITION_EASY = [(150, 150), (150, -150), (-150, 150), (-150, -150)]
POSITION_MEDIUM = [(-160, 160), (-140, 160), (-120, 160), (-100, 160), (-160, 140), (-160, 120), (-160, 100), 
                   (160,160), (160, 140), (160, 120), (160, 100), (140, 160), (120, 160), (100, 160), 
                   (-160, -160), (-160, -140), (-160, -120), (-160, -100), (-140, -160), (-120, -160),
                   (-100, -160), (160, -160), (160, -140), (160, -120), (160, -100), (140, -160), (120, -160),
                   (100, -160), (-80, 80), (80, 80), (80, -80), (-80, -80), (20, 20), (-20, -20),
                   (20, -20), (-20, 20)]
POSITION_HARD = [(230, 230), (70, 230), (-90, 230), (-250, 230), (-170, 110), (-10, 110), (150, 110),
                 (230, -10), (70, -10), (-90, -10), (-250, -10), (-170, -130), (-10, -130), (150, -130),
                 (230, -250), (70, -250), (-90, -250), (-250, -250)]
POSITION_NON_FOOD = []
CHANGE_POSITION = [(10, 10), (10, -10), (-10, 10), (-10, -10)]

class Wall:
    def __init__(self):
        self.walls = []
        
    def create_default_wall(self):
        for x in range(-320, 321, 20):
            position_up = (x, 320)
            position_down = (x, -320)
            self.add_wall(position_up)
            self.add_wall(position_down)
        for y in range(300, -301, -20):
            position_right = (320, y)
            position_left = (-320, y)
            self.add_wall(position_right)
            self.add_wall(position_left)

    def add_wall(self, position):
        new_wall = Turtle("square")
        new_wall.color("red")
        new_wall.penup()
        new_wall.goto(position)
        self.walls.append(new_wall)

    def easy_level(self):
        self.create_default_wall()
        for i in POSITION_EASY:
            for j in CHANGE_POSITION:
                new_x = i[0] + j[0]
                new_y = i[1] + j[1]
                new_position = (new_x, new_y)
                POSITION_NON_FOOD.append(new_position)
                self.add_wall(new_position)

    def medium_level(self):
        self.create_default_wall()
        for i in POSITION_MEDIUM:
            self.add_wall(i)

    def hard_level(self):
        self.create_default_wall()
        for i in POSITION_HARD:
            for j in CHANGE_POSITION:
                new_x = i[0] + j[0]
                new_y = i[1] + j[1]
                new_position = (new_x, new_y)
                POSITION_NON_FOOD.append(new_position)
                self.add_wall(new_position)