STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def up(self):
        """Moves the turtle across the screen"""
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)