   #les bases de python 

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

h=3
i="2"
#convertir str en int 
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
#phrase.count("&") 2h50

#dictonniaire 
user = {
   "nom  ": "dupond",
   "prenom":"jean",
   "age":39
}
print(user)["age"]
print(user)

"nom"in user

print in(user)