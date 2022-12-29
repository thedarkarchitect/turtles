import turtle as t
import random as ran

t.colormode(255)

def colors():
    """random rgb tuple returned"""
    r = ran.randint(0, 255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)

    random_color = (r, g, b)
    return random_color

jam = t.Turtle()
jam.speed(0)

for x in range(0,360,5):
    jam.color(colors())
    jam.setheading(x)
    jam.circle(100)



t.mainloop()

