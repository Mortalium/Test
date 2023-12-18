#This programm is making a Pattern with two triangles formed by 'x' and 'o' characters, witth each row increasing in size.

def triangle(Count,tempCount):
    if(tempCount==Count):
        printx(Count,tempCount,tempCount)
    else:
        printx(Count,tempCount,tempCount)
        triangle(Count,tempCount+1)
        printx(Count,tempCount,tempCount)

def printx(Count,tempCount,tempCount2):
    if(tempCount==0):
        printl(Count-tempCount2+Count+Count-tempCount2)
        printo(tempCount2)
    else:
        print("x",end="")
        printx(Count,tempCount-1,tempCount2)      

def printo(tempCount):
    if(tempCount==0):
        print()
    else:
        print("o",end="")
        printo(tempCount-1)        

def printl(Countl):
    if(Countl!=0):
        print(" ",end="")
        printl(Countl-1)
        
Count=input("Wie breit soll das Dreieck werden?: ")
triangle(int(Count),0)