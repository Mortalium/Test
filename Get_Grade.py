def get_grade(score):
    if(score>=60):
        return "D"
    elif(score>=70):
        return "C"
    elif(score>=80):
        return "B"
    elif(score>=90):
        return "A"
    else:
        return "F"

print(get_grade(85))

#def get_grade(score):
#    if(score>=90):
#        return "D"
#    elif(score>=80):
#        return "C"
#    elif(score>=70):
#        return "B"
#    elif(score>=60):
#        return "A"
#    else:
#        return "F"

#def get_grade(score):
#    return {
#        90<=score<=100: "A",
#        80<=score<90: "B",
#        70<=score<80: "C",
#        60<=score<70: "D",
#        score <60: "F"
#    }.get(True,"Invalid score")

#def get_grade(score):
#    match score:
#        case range(0,59):
#            return "F"
#        case range(60,69):
#            return "D"
#        case range(70,79):
#            return "C"
#        case range(80,89):
#            return "B"
#        case range(90,100):
#            return "A"
#        case _:
#            return "Invalid Score"
