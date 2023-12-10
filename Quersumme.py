Zahlstr=input("Bitte gib eine Zahl ein: ")
Zahlint=int(Zahlstr)
Quersumme=0
for i in range(-len(Zahlstr),0):
    pot=1
    for j in range(0,-i-1):
        pot=pot*10
    rest=Zahlint%pot
    Zahlint=Zahlint-rest
    Zahlint=Zahlint/pot
    Quersumme=Quersumme+Zahlint
    Zahlint=rest
print("Die Quersumme der Zahl ist {}".format(int(Quersumme)))