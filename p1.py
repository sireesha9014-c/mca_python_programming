from turtle import *
speed('fast')
pencolor("black")
pensize(3)

side = 6
for i in range(side):
    for i in range(side):
       fd(50)         # move forward
       lt(360/side)  
    fd(100)
    lt(360/side)  
hideturtle()
mainloop()
