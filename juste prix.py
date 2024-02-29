import random

def consigne():
    mister= random.randint(1, 10)
    choice = int(input("veuillez choisir un nombre entre 1 et 10 "))

    while choice != mister:
        if choice < mister:
            choice = int(input("veuillez choisir un nombre plus grand: "))
        else:
            choice = int(input("veuillez choisir un nombre plus petit : "))

    print("et c'est gagné")

consigne()
         
 