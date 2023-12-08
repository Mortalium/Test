def Sterne(n,l):
    if n==1:
        leer=""
        for i in range(0,l):
            leer=leer+" "
        print(leer + "*")
        return 1
    else:
        Stern=2 + Sterne(n-1,l+1)
        leer=""
        Sterne_Str=""
        for i in range(0,l):
            leer=leer+" "
        for i in range(0,Stern):
            Sterne_Str=Sterne_Str+"*"
        
        print(leer + Sterne_Str)

        return Stern

Zahl=int(input("Wie groß soll der Baum sein?: "))

Stern=Sterne(Zahl,0)

Stamm=((Stern-1)/10)
leer=int(((Stern-1)/2)-Stamm)
Zahl=int(Zahl/3)
Stamm=int((Stamm*2)+1)
for i in range(0,Zahl):
    leerStern=""
    for j in range(0,leer):
        leerStern=leerStern+" "
    for j in range(0,Stamm):
        leerStern=leerStern+"|"
    print(leerStern)