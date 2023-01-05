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

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    #car generator
    car_manager.create_car()
    car_manager.move_car()
    

    #turtle crosses screen
    if player.is_at_finish():
        player.reset()
        car_manager.speed_up()
        scoreboard.change_level()

    #detect collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()