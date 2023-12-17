#Eine Methode soll n (nichtnegative ganze Zahl) Sterne nebeneinander drucken.
def Sterne(n):
    if(n==0):
        print()
    else:
        print("*",end='')
        Sterne(n-1)


def Zahl(n):
    if(n<0):
        print("Bitte wähle eine nichtnegative ganze Zahl, die nicht erst ausgerechnet werden muss!!!")
        n=input("Wie viele Sterne soll ich drucken?: ")
        Zahl(int(n))
    else:
        print()
        Sterne(int(n))
        print()
        print("Ich habe "+str(n)+" Sterne gedruckt")

n=input("Wie viele Sterne soll ich drucken?: ")

Zahl(int(n))