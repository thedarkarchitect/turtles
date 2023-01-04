from turtle import Turtle
import random

class Food(Turtle):#inherited from turtle class so that we can use it's class properties
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)#the turtle is 20 and 0.5 reduces it to 10
        self.color("green")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def new_food(self):
        """sets food to a new location."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)