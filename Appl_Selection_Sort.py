from Appl_Bubble_Sort import CreateList
from Appl_Groesste_Zahl import Max

def SSort(List,Ind):
    if(Ind<len(List)):

        List=SSort(List,Ind+1)

        Maximum=Max(List,Ind,0)

        MInd=List.index(Maximum)

        if(Maximum>List[Ind]):
            List[MInd]=List[Ind]
            List[Ind]=Maximum

        return List
    else:
        return List

def Selection_Sort(List):
    return SSort(List,1)

if(__name__=="__main__"):
    List=CreateList()

    print(List)
    print()

    SList=Selection_Sort(List)

    print()
    print(SList)
