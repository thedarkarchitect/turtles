from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        
    
    def ball_move(self):
        """This will get the ball moving """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        """The ball will bounce down in the positive y"""
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed += 0.9

    def reset_ball(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_x()#this will make the ball go in the oposite because the x coordinates will be flipped on each round