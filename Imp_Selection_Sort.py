from Imp_Bubble_Sort import CreateList
from Groesste_Kleinste_Zahl import Max

def Selection_Sort(List):
    for i in range(len(List)-1,0,-1):
        Maximum=Max(List,i)
        MInd=List.index(Maximum)
        if(Maximum!=List[i]):
            List[MInd]=List[i]
            List[i]=Maximum
    return List

if(__name__=="__main__"):
    List=CreateList()
    print(List)
    print()

    SList=Selection_Sort(List)
    print(SList)
    print()