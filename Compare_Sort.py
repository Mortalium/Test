from Imp_Bubble_Sort import CreateRandList as ImpList
import Appl_Bubble_Sort
import Imp_Bubble_Sort

import time

RandList=ImpList([],500,100)

Applt1=time.time()

ApplSortList=Appl_Bubble_Sort.BBSort(RandList)

Applt2=time.time()

Impt1=time.time()

ImpSortList=Imp_Bubble_Sort.BBSort(RandList)

Impt2=time.time()

if(ApplSortList==ImpSortList):
    print("ApplSortTime: "+str(Applt2-Applt1))
    print("ImpSortTime: "+str(Impt2-Impt1))
else:
    print("Andere Ergebnisse")

#Appl does need more time
#Additionally in python there is a maximum rekursion depth. 
#Because of it the List can't be too long