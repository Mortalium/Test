import Appl_Bubble_Sort

def Count_Value(List,Count):
    if Count>0:
        amount=List[Count]+Count_Value(List,Count-1)
        return amount
    else:
        return List[0]

if(__name__=="__main__"):
    n=int(input("Wie lange soll die Liste sein: "))

    List=[]

    List=Appl_Bubble_Sort.CreateList(List,n)

    amount=Count_Value(List,n-1)

    Mittelwert=float(amount/n)

    print("Der Mittelwert der Liste ist: "+str(Mittelwert))