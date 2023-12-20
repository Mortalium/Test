from Appl_Pot import Pot
def ToBin(Dec,Bin,Count):
    if(Dec!=0):
        if(Dec%Pot(2,Count+1)!=0):
            Dec=Dec-Dec%Pot(2,Count+1)
            Bin="1"+Bin
            return ToBin(Dec,Bin,Count+1)
        else:
            Bin="0"+Bin
            return ToBin(Dec,Bin,Count+1)
    else:
        return Bin

if(__name__=="__main__"):
    Dec=int(input("Wie lautet die Dezimalzahl?: "))
    if(Dec==0):
        print("Die Zahl 0 enthält in jeder Binärstelle nur Nuller z.B. '00000000'")
    else:
        if(Dec<0):
            Dec*=-1
            Vz="-"
        else:
            Vz=""
        Bin=str(ToBin(Dec,"",0))
        print("Die Zahl "+ str(Dec) +" wird als Binärzahl so geschrieben: "+Vz+Bin)