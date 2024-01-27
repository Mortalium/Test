print("Größte/Kleinste Zahl berechnen")
print()

anzahl=input("Wie viele Zahlen sollen verglichen werden?: ")
anzahl= int(anzahl)

print("-------------------")

Array=[]

for x in range(0,anzahl):
    Array.append(input("Zahl: "))

g=Array[0]

for x in range(1,anzahl):
    if Array[x]>g:
        g=Array[x]

print("-------------------")
print("Die größte Zahl ist {}".format(g))
print()

k=Array[0]

for x in range(1,anzahl):
    if Array[x]<k:
        k=Array[x]

print("Die kleinste Zahl ist{}".format(k))
print()