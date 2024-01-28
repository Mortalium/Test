from Appl_Bubble_Sort import CreateList
from Appl_Groesste_Zahl import Max

def Selec_Sort(List,Ind):
    if(Ind<len(List)):

        List=Selec_Sort(List,Ind+1)

        Maximum=Max(List,Ind,0)

        MInd=List.index(Maximum)

        if(Maximum>List[Ind]):
            List[MInd]=List[Ind]
            List[Ind]=Maximum

        return List
    else:
        return List

if(__name__=="__main__"):
    n=int(input("Wie lange soll das Array sein? "))

    List=CreateList(n)

    print(List)
    print()

    SList=Selec_Sort(List,1)

    print()
    print(SList)
