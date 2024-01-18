def BBSort(List):
    global Change
    Change=False
    List=SortList(List,0)
    if Change:
        List=BBSort(List)
        return List
    else:
        return List

def SortList(List,Count):
    if(Count+1<len(List)):
        if(List[Count]>List[Count+1]):
            tmp=List[Count+1]
            List[Count+1]=List[Count]
            List[Count]=tmp
            global Change
            Change=True
        List=SortList(List,Count+1)
        return List
    return List
    
def CreateList(List,n):
    if(n>0):
        Element=int(input("Zahl: "))
        List.append(Element)
        List=CreateList(List,n-1)
        return List
    else:
        return List


if(__name__=="__main__"):
    n=int(input("Wie vile Zahlen sind in der Liste?: "))

    NL=[]

    NL=CreateList(NL,n)

    print(NL)

    NL=BBSort(NL)

    print(NL)