from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        """This controls how the scores are changed"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Arial", 70, "normal"))
        self.goto(100,200)
        self.write(self.right_score, align="Center", font=("Arial", 70, "normal"))

    def left_point(self):
        """adds point to the left player """
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        """adds point to the right player"""
        self.right_score += 1
        self.update_scoreboard()
