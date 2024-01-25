from Appl_Bubble_Sort import CreateList

def Insert_Sort(List,n):
    if(n<len(List)):
        List=Compare(List,n)
        List=Insert_Sort(List,n+1)
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
    
if(__name__=="__main__"):
    n=int(input("Wie viele Elemente soll die Liste enthalten? "))
    print()

    List=CreateList(n)

    print(List)
    print()

    List=Insert_Sort(List,0)

    print(List)
    print()

