import Appl_Bubble_Sort

n=int(input("Wie lange soll die Liste sein: "))

List=[]

List=Appl_Bubble_Sort.CreateList(List,n)

SList=Appl_Bubble_Sort.BBSort(List)

Ind=int(n/2)

if(n%2==0):
    Med=(SList[Ind-1]+SList[Ind])/2
else:
    Med=SList[Ind]

print("Der Median ist "+str(Med))