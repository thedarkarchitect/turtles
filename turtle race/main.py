from turtle import Turtle, Screen
import random


is_race_on = False #controls the race while loop

screen = Screen()
screen.setup(width=500, height=400)

user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
#the list will provide a  color to the racers by index
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#These are the positions where the racers will  line up randomly
y_positions = [-70, -40, -10, 20, 50, 80]

all_racers = []

#Create 6 turtles
for racer_index in range(0, 6):
    racers = Turtle(shape="turtle")
    racers.penup()
    racers.color(colors[racer_index])
    #this position the racers and the x will will be the start line and the y will vary according the index of racer and set position
    racers.goto(x=-230, y=y_positions[racer_index])
    all_racers.append(racers)

if user_choice: #if the user chooses a  color the flag is set to true
    is_race_on = True

while is_race_on:

    for racer in all_racers:
        #230 is 250 - half the width of the turtle.
        if racer.xcor() > 230:#The xcor() return the x coordinate of the racer at their current positon
            is_race_on = False #this flag stops the game
            winning_color = racer.pencolor()#return ths color of the racer that won

            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)#This keeps outputing random intergers between 0 and 10 that can be given to a paticular racer at different for loop instances.
        racer.forward(rand_distance)#making each racer move at a different pixel rate across the screen

screen.exitonclick()