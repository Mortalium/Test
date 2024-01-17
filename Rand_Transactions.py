import random
from datetime import datetime

def create_trans():
    TL=[]
    type_list=["purchase","sale"]
    for i in range(100):
        Type=random.choice(type_list)
        amount=random.randint(1,1000)
        date=datetime.today().strftime('%y-%m-%d')
        date=date[:6]
        if date[3:5] in (1,3,5,7,8,10,12):
            day=random.randint(0,31)
        elif date[3:5] ==2:
            if date[2]%4!=0:
                day=random.randint(0,28)
            else:
                day=random.randint(0,29)
        else:
            day=random.randint(0,30)
        if day<10:
            day="0"+str(day)
        else:
            day=str(day)
        date+=day
        trans={
            "type": Type,
            "amount": amount,
            "date": date
        }
        TL.append(trans)
    return TL

TL=create_trans()

for trans in TL:
    print(trans)

def list_of(my_key,my_type):
    amount_values=0
    for trans in TL:
        if trans['type']==my_type:
            amount_values+=trans[my_key]
    return amount_values

def sum_up(my_type):
    match my_type:
        case 'purchase':
            return list_of("amount","purchase")
        case 'sale':
            return list_of("amount","sale")

income=sum_up("sale")
print("Income: "+str(income))
expenses=sum_up("purchase")
print("Expenses: "+str(expenses))
if(expenses>income):
    print("You lose money!!!")
else:
    print("You make money!!!")