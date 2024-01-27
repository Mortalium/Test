from Appl_Bubble_Sort import CreateList

def Max(List,n,Maximum):
    if n>=0:
        if(List[n]>Maximum):
            Maximum=List[n]
        Maximum=Max(List,n-1,Maximum)
        return Maximum
    else:
        return Maximum

if(__name__=="__main__"):
    n=int(input("Wie lange soll das Array sein? "))

    List=CreateList(n)

    Maximum=Max(List,n-1,0)

    print("Das Maximum der Liste ist "+str(Maximum))