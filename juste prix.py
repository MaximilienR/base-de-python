import random

def consigne():
     mister = random.randint(1, 10)
     try:
             choice = int(input("Veuillez choisir un nombre entre 1 et 10 : "))
             while choice != mister:
                     if choice < mister:
                             choice = int(input("Veuillez choisir un nombre plus grand : "))
                     else:
                             choice = int(input("Veuillez choisir un nombre plus petit : "))
                        
     except ValueError:
             print("Ce n'est pas un chiffre valide.")
     print("C'est gagné !")

consigne()
