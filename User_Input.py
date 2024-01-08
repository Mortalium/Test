rows=int(input("Wie viele Reihen sollen gedruckt werden?: "))

for i in range(1,rows+1):
    for j in range(i):
        print(i,end="")
    print()