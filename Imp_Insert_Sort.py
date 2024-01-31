from Imp_Bubble_Sort import CreateList

def ISort(List):
    for i in range(len(List)-1):
        for j in range(i+1,0,-1):
            if(List[j]<List[j-1]):
                tmp=List[j]
                List[j]=List[j-1]
                List[j-1]=tmp
            else:
                break
    return List

List=CreateList()

print(List)
print()

SList=ISort(List)

print(SList)
print()
