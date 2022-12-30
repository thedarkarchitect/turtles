import turtle as t
import colorsys as cs

t.setup(800,800)
t.speed(0)
t.tracer(10)
t.width(2)
t.bgcolor("black")

for m in range(35):
    for x in range(25):
        t.color(cs.hsv_to_rgb(x/15, m/25, 1))
        t.right(90)
        t.circle(200-m*4, 90)
        t.left(90)
        t.circle(200-m*4, 90)
        t.right(180)
        t.circle(50, 24)

t.hideturtle()
t.done()