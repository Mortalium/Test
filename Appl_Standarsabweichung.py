import Appl_Bubble_Sort

from Appl_Mittelwert import Count_Value

from Appl_Pot import Pot

import math

def Stand_abw(List,n):
    Mittelwert=Count_Value(List,n-1)/n

    Varianz_Value=Varianz(List,Mittelwert,0,0)

    Standartabweichung=math.sqrt(Varianz_Value)

    return Standartabweichung

def Varianz(List,Mittelwert,Ind,Abw):
    if Ind<len(List):
        Abw=Abw+Pot(List[Ind]-Mittelwert,2)
        Abw=Varianz(List,Mittelwert,Ind+1,Abw)
        return Abw
    else:
        return Abw/len(List)



n=int(input("Wie lange soll die Liste sein: "))

List=[]

List=Appl_Bubble_Sort.CreateList(List,n)

Stand_abw(List,n)

print("Die Standartabweichung ist "+str(Standartabweichung))