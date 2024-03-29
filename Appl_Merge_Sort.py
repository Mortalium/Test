from Appl_Bubble_Sort import CreateList

def Merge_Sort(List):
    if(len(List)==1):
        return List
    else:
        mid=int(len(List)/2)
        L1=Merge_Sort(List[:mid])
        L2=Merge_Sort(List[mid:])
        List=Compare([],L1,L2)
        return List

def Compare(List,L1,L2):
    if(len(L1)==0 or len(L2)==0):
        List=List+L1+L2
        return List
    else:
        if(L1[0]<L2[0]):
            List.append(L1[0])
            L1.pop(0)
        else:
            List.append(L2[0])
            L2.pop(0)
        List=Compare(List,L1,L2)
        return List

if(__name__=="__main__"):
    List=CreateList()

    print(List)
    print()

    List=Merge_Sort(List)
    print(List)
    print()