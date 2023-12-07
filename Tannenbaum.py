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

Sterne(Zahl,0)