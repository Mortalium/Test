import turtle
import math
from Appl_Pot import Pot

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
        case '4':
            Four(Dir)
        case '5':
            Five(Dir)
        case '6':
            Six(Dir)
        case '7':
            Seven(Dir)
        case '8':
            Eight(Dir)
        case '9':
            Nine(Dir)
        case '10':
            Ten(Dir)

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
            t1.forward(30)
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
            t1.forward(42.5)
            t1.right(90)
            t1.forward(7.5)
            t1.pendown()
    t1.right(180)
    t1.circle(7.5,-270)
    t1.right(180)
    t1.circle(7.5,-270)

def Four(Dir):
    One(Dir)
    t1.forward(5)
    t1.left(135)
    t1.forward(math.sqrt(Pot(20,2)/2)+5)

def Five(Dir):
    match Dir:
        case 'Right':
            t1.penup()
            t1.back(20)
            t1.left(90)
            t1.back(7.5)
            t1.pendown()
        case 'UP':
            t1.penup()
            t1.forward(45)
            t1.right(90)
            t1.forward(15)
            t1.left(90)
            t1.back(15)
            t1.pendown()
    t1.forward(15)
    t1.left(90)
    t1.forward(10)
    t1.right(90)
    t1.back(5)
    t1.circle(10,-180)
    t1.back(5)

def Six(Dir):
    match Dir:
        case 'Right':
            t1.penup()
            t1.back(20)
            t1.left(90)
            t1.back(7.5)
            t1.pendown()
        case 'UP':
            t1.penup()
            t1.forward(30)
            t1.right(90)
            t1.forward(15)
            t1.left(90)
            t1.pendown()
    t1.circle(15,155)
    t1.left(10)
    t1.circle(7)

def Seven(Dir):
    match Dir:
        case 'Right':
            t1.penup()
            t1.back(50)
            t1.left(90)
            t1.forward(7.5)
            t1.pendown()
        case 'UP':
            t1.penup()
            t1.forward(45)
            t1.left(90)
            t1.forward(15)
            t1.right(90)
            t1.pendown()
    Angle=math.atan(30/15)*180/math.pi
    t1.right(180-Angle)
    t1.forward(math.sqrt(Pot(30,2)+Pot(15,2)))
    t1.setheading(180)
    t1.forward(15)
    t1.penup()
    t1.left(90)
    t1.forward(15)
    t1.right(90)
    t1.back(12.5)
    t1.pendown()
    t1.forward(10)

def Eight(Dir):
    match Dir:
        case 'Right':
            t1.penup()
            t1.back(35)
            t1.left(90)
            t1.pendown()
        case 'UP':
            t1.penup()
            t1.forward(37.5)
            t1.pendown()
    t1.circle(7.5)
    t1.right(180)
    t1.circle(7.5)

def Nine(Dir):
    match Dir:
        case 'Right':
            t1.penup()
            t1.back(50)
            t1.right(90)
            t1.back(7.5)
            t1.pendown()
        case 'UP':
            t1.penup()
            t1.forward(45)
            t1.left(90)
            t1.forward(15)
            t1.left(90)
            t1.pendown()
    t1.circle(15,155)
    t1.left(10)
    t1.circle(7)

def Ten(Dir):
    match Dir:
        case 'Right':
            t1.penup()
            t1.back(50)
            t1.left(90)
            t1.forward(5)
            t1.right(90)
            t1.pendown()
        case 'UP':
            t1.penup()
            t1.forward(55)
            t1.left(90)
            t1.forward(15)
            t1.right(180)
            t1.pendown()
    Pos=t1.pos()
    One("NONE")
    t1.penup()
    t1.setpos(Pos[0],Pos[1])
    t1.setheading(0)
    t1.forward(10)
    t1.left(90)
    t1.forward(7.5)
    t1.right(180)
    t1.pendown()
    t1.circle(7.5,180)
    t1.forward(15)
    t1.circle(7.5,180)
    t1.forward(15)
    
def print_func():
    func=input("Welche Funktion (Parabel, ) soll geplotted werden? ")
    match func:
        case "Parabel":
            t1.penup()
            t1.setpos(SPosX,SPosY+Parabel_func(0))
            t1.pendown()
            for i in range(1,501):
                t1.setpos(SPosX+i,SPosY+Parabel_func(i))
            pass
        case _:
            print("Wrong input!")
            print()
            print_func()
            pass

def Parabel_func(x):
    Kla=(x/50)-5
    y_pos=(Pot(Kla,2)*50)/2.5
    return y_pos

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

print_func()

turtle.done()