from turtle import *

def draw_star():
    speed(3)
    bgcolor("Purple")
    pensize(5)
    pencolor("yellow")
    penup()
    goto(100,100)
    seth(180)
    pendown()
    goto(-100,100)
    seth(300)
    goto(0,-100)
    seth(60)
    goto(100,100)
    begin_fill()
    penup()
    goto(0,150)
    seth(240)
    pendown()
    goto(-100,-50)
    seth(0)
    goto(100,-50)
    seth(120)
    goto(0,150)
    # goto()
    done()
    
draw_star()