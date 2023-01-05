COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.car_generator()


    def car_generator(self):
        new_y = random.randint(-270,270)
        self.color(random.choice(COLORS))
        self.goto(-280, new_y)
        self.setheading(180)
        self.forward(STARTING_MOVE_DISTANCE)
        
    def move_faster(self):
        pass
