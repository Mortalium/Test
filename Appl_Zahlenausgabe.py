#Eine Methode soll abwärts die Zahlen von n bis 1 ausgeben.
def GibZahlausvon(n):
    if(n>0):
        print(n)
        GibZahlausvon(n-1)

def Eingabe():  
    Zahl=input("Ab welcher Zahl (nur positive Zahlen) soll abwärts gezählt werden?: ")
    try:
        Zahl=int(Zahl)
        if(Zahl>0):
            GibZahlausvon(Zahl)
        else:
            print("Bitte gib einen positiven Integerwert an (ohne, dass der Computer diesen erste errechnen muss)")
        Eingabe()
    except:
        print("Bitte gib einen positiven Integerwert an (ohne, dass der Computer diesen erste errechnen muss)")
        Eingabe()
    
Eingabe()