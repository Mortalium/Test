import random

n=int(input("Wie lange soll die Liste sein? "))
print()

List=[]

mode=input("Manuell (man) oder Random (rand)? ")
print()

match mode:
    case "man":
        for i in range(n):
            Zahl=int(input("Zahl "+i+": "))
            List.append(Zahl)
    case "rand":
        Limit=int(input("Limit: "))
        for i in range(n):
            Zahl=random.randint(0,Limit)
            List.append(Zahl)

print(List)

SList=List.copy()

change=True

while change:
    change=False
    for i in range(n-1):
        if(SList[i]>SList[i+1]):
            tmp=SList[i]
            SList[i]=SList[i+1]
            SList[i+1]=tmp
            change=True

print(SList)