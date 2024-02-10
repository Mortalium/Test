import random

def BBSort(List):
    List,Change=SortList(List,0,False)
    if Change:
        List=BBSort(List)
        return List
    else:
        return List

def SortList(List,Count,Change):
    if(Count+1<len(List)):
        if(List[Count]>List[Count+1]):
            tmp=List[Count+1]
            List[Count+1]=List[Count]
            List[Count]=tmp
            Change=True
        List,Change=SortList(List,Count+1,Change)
        return List,Change
    return List,Change

def CreateList():
    List=[]
    n=int(input("Wie lange soll die Liste sein? "))
    print()
    manrand=input("Soll die liste manuell(man) oder random(rand) befüllt werden? ")
    print()
    match manrand:
        case "man":
            return CreateManList(List,n)
        case "rand":
            Limit=int(input("Limit: "))
            print()
            return CreateRandList(List,n,Limit)
        case _:
            print("Wrong input!")
            print()
            return CreateList(n)       

def CreateManList(List,n):
    if(n>0):
        Element=int(input("Zahl: "))
        List.append(Element)
        List=CreateManList(List,n-1)
        return List
    else:
        return List
    
def CreateRandList(List,n,Limit):
    if(n>0):
        Element=random.randint(1,Limit)
        List.append(Element)
        List=CreateRandList(List,n-1,Limit)
        return List
    else:
        return List


if(__name__=="__main__"):
    NL=CreateList()

    print(NL)
    print()

    NL=BBSort(NL)

    print(NL)
    print()