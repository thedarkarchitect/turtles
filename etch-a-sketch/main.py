from turtle import Turtle, Screen

kev = Turtle()
screen = Screen()


def move_forwards():
    kev.forward(10)

def move_backwards():
    kev.backward(10)

def turn_left():
    #heading return the current turtle position
    new_heading = kev.heading() + 10
    kev.setheading(new_heading)

def turn_right():
    new_heading = kev.heading() - 10
    kev.setheading(new_heading)

def clear():
    kev.clear()
    kev.penup()
    kev.home()
    kev.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
