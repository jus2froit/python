import random

students = ["Alexandre.C","Benoît","Donatien","Hugo","Myriam",
    "Nicolas","Vlad","Quentin R","Quentin F","Steven","Julian","Maxence","Thomas","Amandine", "Tristan"]

def tirageGroupe(students):
    for nbGroupe in range (1,(( len(students) // 3)+1)):
        print (nbGroupe)
        for numeroStudent in range (3):
            numeroStudent = random.randint(0, (len(students)-1))
            print(students[numeroStudent])
            del students[numeroStudent]
        print("----------------------------------")
    return(students)

print(tirageGroupe(students))