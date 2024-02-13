import random

def CreateList():
    n=int(input("Wie lange soll die Liste sein? "))
    print()

    List=[]
    mode=input("Manuell (man) oder Random (rand)? ")
    print()

    match mode:
        case "man":
            List=CreateManList(List,n)
        case "rand":
            Limit=int(input("Limit: "))
            print()
            List=CreateRandList(List,n,Limit)
    return List

def CreateManList(List,n):
    for i in range(n):
        Zahl=int(input("Zahl "+i+": "))
        List.append(Zahl)
    return List

def CreateRandList(List,n,Limit):
    for i in range(n):
        Zahl=random.randint(0,Limit)
        List.append(Zahl)
    return List

def BBSort(List):
    change=True
    while change:
        change=False
        for i in range(1,len(List)):
            if(List[i-1]>List[i]):
                tmp=List[i-1]
                List[i-1]=List[i]
                List[i]=tmp
                change=True
    return List

if(__name__=="__main__"):
    List=CreateList()

    print(List)

    SList=BBSort(List)

    print(SList)