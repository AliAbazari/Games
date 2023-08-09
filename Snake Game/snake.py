from turtle import Turtle

POSITION_EASY_MEDIUM = [(0, 0), (-20, 0), (-40, 0)]
POSITION_HARD = [(0, 20), (-20, 20), (-40, 20)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self, level):
        self.segments = []
        self.create_snake(level)
        self.head = self.segments[0]

    def create_snake(self, level):
        if level == "Easy" or level == "Medium":
            for position in POSITION_EASY_MEDIUM:
                self.add_segment(position)
        elif level == "Hard":
            for position in POSITION_HARD:
                self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)