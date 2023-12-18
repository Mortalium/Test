#Die Potenz pot(x, y) = xy (x vom Typ double, y ganze Zahl) soll berechnet werden.
def Pot(Basis,Potenz):
    if(Potenz==0):
        return 1
    else:
        if(Potenz>0):
            return Basis*Pot(Basis,Potenz-1)
        else:
            return 1/Pot(Basis,Potenz*(-1))

Basis=input("Wie lautet die Basis?: ")
Potenz=input("Wie lautet die Potenz?: ")

Produkt=str(Pot(int(Basis),int(Potenz)))

print("Das Ergebnis von " + Basis + " hoch " + Potenz + " ist " + Produkt)