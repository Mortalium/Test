from Imp_Bubble_Sort import CreateList

def QSort(List):
    if(len(List)<=1):
        return List
    else:
        ListR,ListL=Split(List,1,[],[])
        
        List=QSort(ListL)+List[:1]+QSort(ListR)
        return List

def Split(List,i,ListR,ListL):
    if(i<len(List)):
        if(List[i]<List[0]):
            ListL.append(List[i])
        else:
            ListR.append(List[i])
        ListR,ListL=Split(List,i+1,ListR,ListL)
        return ListR,ListL
    else:
        return ListR,ListL

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