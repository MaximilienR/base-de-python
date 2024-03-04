print("*****MENU*****")

def afficher_menu():
 
    a=print("1. fr")
    b= print("2. en")
    c=print("3. spa")

afficher_menu() 
 

choice= int(input("veuillez choisir un nombre "));     


match choice:
   case 1 :
      print("bonjour")
   case 2:
      print("hello")
   case 3:
      print("ola")
   case _:
      print("aucun resultat ")