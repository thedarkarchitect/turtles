import turtle as t

kev = t.Turtle()

for i in range(10):
    kev.forward(10)
    kev.penup()
    kev.forward(10)
    kev.pendown()

t.mainloop()