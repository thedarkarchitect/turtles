import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

for i in range(20):
    car_manager.car_generator()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    #car generator
    

    #turtle collides with car

    #turtle crosses screen
    if player.ycor() > 290:
        player.reset()

    #detect collision
    if player.distance(car_manager) < 10:
        game_is_on = False
        scoreboard.game_over()



screen.exitonclick()