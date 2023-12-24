import turtle

t1=turtle.Turtle()

def AxisPart(Count,Num,Dir):
    if(Count>=0):
        t1.left(90)
        t1.forward(10)
        t1.back(20)
        t1.forward(10)
        Number(Num,Dir)
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

def One(Dir):
    match Dir:
        case 'Right':
            t1.penup()
            t1.back(50)
            t1.pendown()
            t1.forward(30)
            t1.left(135)
            t1.forward(15)
            t1.penup()
            t1.back(15)
            t1.right(135)
            t1.forward(20)
            t1.pendown()
        case 'UP':
            t1.penup()
            t1.right(180)
            t1.back(30)
            t1.left(90)
            t1.back(15)
            t1.pendown()
            t1.forward(30)
            t1.left(135)
            t1.forward(15)
            t1.penup()
            t1.back(15)
            t1.right(135)
            t1.back(15)
            t1.right(90)
            t1.forward(30)
            t1.right(180)
            t1.pendown()

#def Two(Dir):
 #   match Dir:
  #      case 'Right':

   #     case 'UP':

SPosX=-200
SPosY=-200

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