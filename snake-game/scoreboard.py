from turtle import Turtle 
FONT = ("Arial", 10, "normal")
ALIGN = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.num}", align=ALIGN, font=FONT)
        

    def new_score(self):
        """When food is hit the score will increase"""
        self.clear()
        self.num += 1
        self.write(f"Score: {self.num}", align=ALIGN, font=FONT)

    def game_over(self):
        """indicates the game is over"""
        self.goto(0,0)
        self.write("GAMEOVER", align=ALIGN, font=("Arial", 24, "bold"))