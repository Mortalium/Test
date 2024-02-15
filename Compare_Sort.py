import sys
sys.setrecursionlimit(10000000)

from Imp_Bubble_Sort import CreateRandList
import Appl_Bubble_Sort
import Imp_Bubble_Sort
import Appl_Insert_Sort
import Imp_Insert_Sort

import time

RandList=CreateRandList([],5000,100)

ApplBBt1=time.time()

ApplSortList=Appl_Bubble_Sort.BBSort(RandList.copy())
#I have to copy the List because if I don't it will get sorted (global variable)

ApplBBt2=time.time()

ImpBBt1=time.time()

ImpSortList=Imp_Bubble_Sort.BBSort(RandList.copy())

ImpBBt2=time.time()

if(ApplSortList==ImpSortList):
    print("Bubble Sort: ")
    print()
    print("ApplSortTime: "+str(ApplBBt2-ApplBBt1))
    print("ImpSortTime: "+str(ImpBBt2-ImpBBt1))
    print()
else:
    print("Andere Ergebnisse")

#Appl does need more time

ApplInsertt1=time.time()

ApplSortList=Appl_Insert_Sort.Insert_Sort(RandList.copy())

ApplInsertt2=time.time()

ImpInsertt1=time.time()

ImpSortList=Imp_Insert_Sort.Insert_Sort(RandList.copy())

ImpInsertt2=time.time()

if(ApplSortList==ImpSortList):
    print("Insert Sort: ")
    print()
    print("ApplSortTime: "+str(ApplInsertt2-ApplInsertt1))
    print("ImpSortTime: "+str(ImpInsertt2-ImpInsertt1))
    print()
else:
    print("Andere Ergebnisse")

#Appl needs more time