from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__()
        self.paddle_position = paddle_position
        self.color("White")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.paddle_position)

    def up(self):
        new_y = self.ycor() +  20
        self.goto(self.xcor(), new_y)
        
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)