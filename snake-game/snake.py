from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        #calls the create_snake method once the class is called as an instance
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        #makes the snake
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)



    def move(self):
        for seg_num in range(len(self.segments) -1 , 0, -1):#this for loop will get the last segment to move to the position of the one infront of it 
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        """this will move the snake up after checking if the snake is not moving down so the snake doesnt move on itself"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """this will move the snake down after checking if the snake is not moving up so the snake doesnt move on itself"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    
    def left(self):
        """this will move the snake left after checking if the snake is not moving right so the snake doesnt move on itself"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """this will move the snake right after checking if the snake is not moving left so the snake doesnt move on itself"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)