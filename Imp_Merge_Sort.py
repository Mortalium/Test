from Imp_Bubble_Sort import CreateList

def MSort(List):
    if(len(List)==1):
        return List
    else:
        mid=int(len(List)/2)
        L1=MSort(List[:mid])
        L2=MSort(List[mid:])
        List.clear()
        i=0
        j=0
        while(i<len(L1) and j<len(L2)):
            if(L1[i]<L2[j]):
                List.append(L1[i])
                i+=1
            else:
                List.append(L2[j])
                j+=1
        if(len(L1)>i):
            List=List+L1[i:]
        elif(len(L2)>j):
            List=List+L2[j:]
        return List

if(__name__=="__main__"):
    List=CreateList()

    print(List)
    print()

    MSort(List)
    print(List)
    print()