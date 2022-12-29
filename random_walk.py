import turtle as t
import random

#sets the color to recieve the rgb format of colors
t.colormode(255)

angles = [90, 180, 270, 0]

def colors():
    """random rgb tuple returned"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color


rog = t.Turtle()
rog.speed(0)
rog.pensize(10)

for i in range(1000):
    rog.color(colors())
    rog.setheading(random.choice(angles))
    rog.forward(20)


t.mainloop()