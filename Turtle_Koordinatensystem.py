import turtle
import math

t1=turtle.Turtle()

def AxisPart(Count,Num,Dir):
    if(Count>=0):
        t1.left(90)
        t1.forward(10)
        t1.back(20)
        t1.forward(10)
        Pos=t1.pos()
        Number(Num,Dir)
        t1.penup()
        t1.setpos(Pos[0],Pos[1])
        t1.pendown()
        if(Dir=="Right"):
            t1.setheading(90)
        else:
            t1.setheading(180)
        t1.right(90)
        t1.forward(50)
        AxisPart(Count-1,Num+1,Dir)
    else:
        t1.left(90)
        t1.forward(10)
        t1.right(120)
        t1.forward(20)
        t1.right(120)
        t1.forward(20)
        t1.right(120)
        t1.forward(10)
        
                

def Number(Number,Dir):
    Number=str(Number)
    match Number:
        case '1':
            One(Dir)
        case '2':
            Two(Dir)
        case '3':
            Three(Dir)

def One(Dir):
    match Dir:
        case 'Right':
            t1.penup()
            t1.back(50)
            t1.pendown()
        case 'UP':
            t1.penup()
            t1.forward(30)
            t1.right(90)
            t1.back(15)
            t1.pendown()
    t1.forward(30)
    t1.left(135)
    t1.forward(15)

def Two(Dir):
    match Dir:
        case 'Right':
            t1.penup()
            t1.back(30)
            t1.right(90)
            t1.forward(10)
            t1.left(90)
            t1.pendown()
        case 'UP':
            t1.penup()
            t1.forward(25)
            t1.right(135)
            t1.forward(5*math.sqrt(2))
            t1.left(45)
            t1.pendown()
    t1.circle(10,180)
    t1.circle(10,-180)
    t1.setheading(-135)
    t1.forward(20*math.sqrt(2))
    t1.left(135)
    t1.forward(20)

def Three(Dir):
    match Dir:
        case 'Right':
            t1.penup()
            t1.back(27.5)
            t1.left(90)
            t1.forward(7.5)
            t1.right(90)
            t1.pendown()
        case 'UP':
            t1.penup()
            t1.forward(37.5)
            t1.right(90)
            t1.forward(7.5)
            t1.pendown()
    t1.right(180)
    t1.circle(7.5,-270)
    t1.right(180)
    t1.circle(7.5,-270)

SPosX=-200
SPosY=-200

t1.speed(0)
t1.hideturtle()

t1.penup()
t1.setpos(SPosX,SPosY)
t1.pendown()

t1.back(50)
t1.forward(50)
AxisPart(10,0,"Right")

t1.penup()
t1.setpos(SPosX,SPosY)
t1.pendown()

t1.back(50)
t1.forward(50)
AxisPart(10,0,"UP")

turtle.done()