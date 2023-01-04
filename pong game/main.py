from turtle import Screen, Turtle
from paddleA import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PonG")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    #ball should move
    ball.ball_move()
        
    #wall detection 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect  ball goes out of bounds on right
    if ball.xcor() > 350:
        ball.reset_ball()
    
    #detect ball goes outof bounds on left
    if ball.xcor() < -350:
        ball.reset_ball()
        
screen.exitonclick()