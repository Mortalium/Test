import random

def CreateList():
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
    return List

def BBSort(List):
    change=True

    while change:
        change=False
        for i in range(len(List)):
            if(List[i]>List[i+1]):
                tmp=List[i]
                List[i]=List[i+1]
                List[i+1]=tmp
                change=True
    return List

if(__name__=="__main__"):
    List=CreateList()

    print(List)

    SList=BBSort(List)

    print(SList)