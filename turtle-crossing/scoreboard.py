FONT = ("Courier", 24, "bold")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto((-270,250))
        self.update_level()
        
    def update_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)
    
    def change_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        """Displays game over on the screen"""
        self.write("GAME OVER", align="center", font=FONT)