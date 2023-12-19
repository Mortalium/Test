import turtle
import math

def draw(Lenght):
    if(Lenght<5):
        #Nothin
        Lenght=Lenght
    else:
        Lenght*=0.95
        t1.forward(Lenght)
        t1.left(120)
        Lenght*=0.95
        t1.forward(Lenght)
        t1.left(120)
        Lenght*=0.95
        t1.forward(Lenght)
        t1.left(120)
        draw(Lenght)

t1 = turtle.Turtle()
t1.hideturtle()
t1.penup()
Lenght=int(input("Size of the Triangle?: "))
PointMiddle=(math.sqrt((Lenght*Lenght)-(Lenght/2)*(Lenght/2)))/2
t1.setpos(-Lenght/2,-PointMiddle)
t1.pendown()
draw(Lenght)

turtle.done()