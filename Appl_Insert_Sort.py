from Appl_Bubble_Sort import CreateList

def In_Sort(List,n):
    if(n<len(List)):
        List=Compare(List,n)
        List=In_Sort(List,n+1)
        return List
    else:
        return List


def Compare(List,n):
    if(n>0):
        if(List[n]<List[n-1]):
            temp=List[n]
            List[n]=List[n-1]
            List[n-1]=temp
            List=Compare(List,n-1)
            return List
        else:
            return List
    else:
        return List

def Insert_Sort(List):
    return In_Sort(List,0)

if(__name__=="__main__"):
    List=CreateList()

    print(List)
    print()

    List=Insert_Sort(List)

    print(List)
    print()

