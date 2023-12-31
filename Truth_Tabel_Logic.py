def AND(a,b):
    if a!=0 and a==b:
        return "1"
    else:
        return "0"
   
def NAND(a,b):
    return NOT(AND(a,b))

def OR(a,b):
    if a==1 or b==1:
        return "1"
    else:
        return "0"

def XOR(a,b):
    if (OR(a,b)=="1") and (not a==b):
        return "1"
    else:
        return "0"

def NOT(a):
    a=int(a)
    return str((a+1)%2)

def NOR(a,b):
    return NOT(OR(a,b))

def XNOR(a,b):
    return NOT(XOR(a,b))

def Table(Logic):
    if Logic!="NOT":
        print("A",end="")
        for i in range(10):
            print(" ",end="")
        print("B",end="")
        for i in range(10):
            print(" ",end="")
        print(Logic)
        
        for i in range(30):
            print("-",end="")
        print()

        print("1",end="")
        for i in range(10):
            print(" ",end="")
        print("1",end="")
        for i in range(10):
            print(" ",end="")
        print(GATE(Logic,1,1))

        print("1",end="")
        for i in range(10):
            print(" ",end="")
        print("0",end="")
        for i in range(10):
            print(" ",end="")
        print(GATE(Logic,1,0))

        print("0",end="")
        for i in range(10):
            print(" ",end="")
        print("1",end="")
        for i in range(10):
            print(" ",end="")
        print(GATE(Logic,0,1))

        print("0",end="")
        for i in range(10):
            print(" ",end="")
        print("0",end="")
        for i in range(10):
            print(" ",end="")
        print(GATE(Logic,0,0))
    else:
        print("A",end="")
        for i in range(10):
            print(" ",end="")
        print(Logic)

        print("1",end="")
        for i in range(10):
            print(" ",end="")
        print(GATE(Logic,1,0))

        print("0",end="")
        for i in range(10):
            print(" ",end="")
        print(GATE(Logic,0,0))

def GATE(Logic,a,b):
    match Logic:
        case "AND":
            return AND(a,b)
        case "NAND":
            return NAND(a,b)
        case "OR":
            return OR(a,b)
        case "XOR":
            return XOR(a,b)
        case "NOT":
            return NOT(a)
        case "NOR":
            return NOR(a,b)
        case "XNOR":
            return XNOR(a,b)

Print=True
while Print:
    Logic=input("Which logic gate (AND, OR, XOR, NOT, NAND, NOR, XNOR) should be printed? ")
    print()

    Table(Logic)
    
    print()
    if input("Again?[j/n]") =="n":
        Print=False