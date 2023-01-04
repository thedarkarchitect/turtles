from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake xEnzia")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()#this stops the animation from spliting while it travel across the screen by refreshing the screen every 0.1 seconds using the sleep function
    time.sleep(0.1)

    snake.move()
    
    #detect collision with food 
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        score.new_score()

    #detect collision with the wall
    if  snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()



screen.exitonclick()