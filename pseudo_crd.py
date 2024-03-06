import sys

print("*****MENU*****")
print("Choisissez parmi les 5 options suivantes :")

LISTE=[]

MENU="""Veuillez choisir l'une des options suivantes:
     1 : Ajouter un élément à la liste
     2 : Afficher la liste 
     3 : Vider la liste
     4. Quitter
        Choix séléectioné: """
        
CHOICES_MENU=["1","2","3","4","5"]
 

while True:
    user_choice=""
    while user_choice not in CHOICES_MENU:
        user_choice=input(MENU)
        if user_choice not in CHOICES_MENU:
            print("veuillez saisir un chooix parmit la liste")
    
    if user_choice=="1":
        product=input("veuillez indiquer le nom de votre produit : ")
        LISTE.append(product)
        print(f"l'élement {product} a bien était enregistré")
    elif user_choice=="2":
        print(f"votre liste contient les produits : {LISTE}")
    elif user_choice=="3":
        LISTE.clear()
        print(f"la liste bien était supprimer")
    elif user_choice=="4":
        print("merci de votre visite à très bientot")
        sys.exit()
 

        
 