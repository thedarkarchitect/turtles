import turtle as t
import random 

colors = ['blue', 'yellow', 'red', 'orange', 'cyan', 'green']

kev = t.Turtle()

def draw_shape():
    
    for i in range(3,11):
        angle = 360 / i
        kev.pencolor(random.choice(colors))
        for m in range(i):
            #This does the movement the number of times the side of the shape is 
            kev.forward(70)
            kev.right(angle)



draw_shape()

t.mainloop()