COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.cars = []#This will store all the cars so that we can make them move each
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """make a new car """
        #To control the rate at which the cars are created we use probabitilyt of creating a car every 6 times
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle('square')
            car.shapesize( stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            new_y = random.randint(-240, 250)
            car.goto(290, new_y)
            self.cars.append(car)
        
    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
