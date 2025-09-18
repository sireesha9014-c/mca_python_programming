from turtle import *

speed(-1)      # fastest drawing
side = 6

for i in range(side):
    for j  in range(side - 1):
        for k in range(side - 1):
            fd(25)
            lt(360 / (side - 1))
        fd(50)
        lt(360 / (side - 1))
    fd(100)
    lt(360 / side)

hideturtle()
mainloop()
