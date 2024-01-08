Prime=int(input("Number to test: "))

for i in range(2,Prime+1):
    if Prime%i==0:
        Is_Prime=True
        break
    else:
        Is_Prime=False

print(Is_Prime)