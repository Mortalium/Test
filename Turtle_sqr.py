import turtle
wn=turtle.Screen()
wn.bgcolor("light green")
t1 =turtle.Turtle()
t1.color("blue")

def sqrfunc(size):
    for i in range(4):
        t1.fd(size)
        t1.left(90)
        size=size+5

size=int(input("Gib die kleinste länge ein: "))

for i in range(size,size+7*20,20):
    sqrfunc(i)

turtle.done()