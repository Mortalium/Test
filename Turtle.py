import turtle

t1 = turtle.Turtle()
 
def printt(Length,Count):
    if(Count==1):
        t1.forward(Length)
        t1.left(60)
        t1.forward(Length)
        t1.right(120)
        t1.forward(Length)
        t1.left(60)
        t1.forward(Length)
    else:
        printt(Length/3,Count-1)
        t1.left(60)
        printt(Length/3,Count-1)
        t1.right(120)
        printt(Length/3,Count-1)
        t1.left(60)
        printt(Length/3,Count-1)

Count=input("Wie viele Rekursionen soll es geben?: ")
Length=input("Wie lang soll gezeichnet werden?: ")
t1.setpos(-int(Length)*1.5,0)
printt(int(Length),int(Count))
t1.backward(int(Length)*1.5)
turtle.done()