from Imp_Bubble_Sort import CreateList

def QSort(List):
    if(len(List)<=1):
        return List
    else:
        List,Pivot=PivCompare(List,0,len(List),0,len(List)-1)
        List=QSort(List[:Pivot])+[List[Pivot]]+QSort(List[Pivot+1:])
        return List

def PivCompare(List,Pivot,LPivot,LMin,RMax):
    if(Pivot!=LPivot):
        LPivot=Pivot
        List,Pivot,RMax=for_CompareNeg(List,Pivot,RMax,RMax)

        List,Pivot,LMin=for_ComparePos(List,Pivot,LMin,LMin)
        
        List,Pivot=PivCompare(List,Pivot,LPivot,LMin,RMax)
        return List,Pivot
    else:
        return List,Pivot

def for_CompareNeg(List,Pivot,RMax,i):
    if(i>Pivot):
        if(List[Pivot]>List[i]):
            tmp=List[Pivot]
            List[Pivot]=List[i]
            List[i]=tmp
            Pivot=i
            RMax=Pivot-1
            return List,Pivot,RMax
        else:
            List,Pivot,RMax=for_CompareNeg(List,Pivot,RMax,i-1)
            return List,Pivot,RMax
    else:
        return List,Pivot,RMax

def for_ComparePos(List,Pivot,LMin,i):
    if(i<Pivot):
        if(List[Pivot]<=List[i]):
            tmp=List[Pivot]
            List[Pivot]=List[i]
            List[i]=tmp
            Pivot=i
            LMin=Pivot+1
            return List,Pivot,LMin
        else:
            List,Pivot,LMin=for_ComparePos(List,Pivot,LMin,i+1)
            return List,Pivot,LMin
    else:
        return List,Pivot,LMin

def Quick_Sort(List):
    if(len(List)<1):
        return "Error"
    else:
        return QSort(List)

if(__name__=="__main__"):
    List=CreateList()

    print(List)
    print()

    SList=Quick_Sort(List)
    if(type(SList)=="str"):
        print("Error!!!")
        print("List has no elements!")
    else:
        print(SList)
        print()