   #les bases de python 

 #menu 
print("**************MENU*************")
def afficher_menu():
        print("=== MENU ===")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        choix = input("Entrez votre choix (1-4) : ")
        
        return choix
     
afficher_menu()     
 
#les variable + faire un demande utilisateur 
identity = input("veuillez saisir votre nom"+ " " );
#affectation multiple 
c,d=45,46
e=f=g=50;
#afficher le texte+concacténation
print ('bonjour '+ ' '+ identity+f'content de te voir');

"bonjour".replace("jour","soir")
#utiliser les chiffre
grandFrere =int(2)
petitFrere = int(5)
ageTT= grandFrere+petitFrere
print(ageTT)


#convertir str en int 
i="2"
h=3
i=int(i) 
print(h+i)
#liste (différence liste et tuple le tuple ne peut etre modifié on dit qu'il est immutable de plus on utilise des parranthèse au lieu des crochets )
ma_liste=["pomme","banane","orange"]
ma_liste_2=[5,1,3]
del ma_liste_2[1]
print(ma_liste[0])
ma_liste[0]="fraise"
print(ma_liste)
print(ma_liste_2)
 
#split
liste="1,2,3,4,5".split(",")
print(liste);

#compter les caratectre 
#phrase ="combien y a t il de mot dans ma phrase "
#phrase.count("&") 

#dictonniaire 
user = {
   "nom  ": "dupond",
   "prenom":"jean",
   "age":39
} 
print(user)

"nom"in user

print in(user)
#verrifier la fin d'un document
fin=("image.png")
fin.endswith(".png")

#la fonction match ! le "_" veut dire les cas n'ont définit 

poste = "cjanteur"
 

match poste:
   case"employe":
      print("1200")
   case"mangeur":
      print("2000")
   case"director":
      print("3000")
   case _:
      print("aucun resultat ")
    
      
  