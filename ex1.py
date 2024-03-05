 
 
a=str(10)+ ' ' +'+'+'5'+' '+'égal 15'#10 +5 est égal à 15 
b=10+int('5')#15 OK
c=("L'addition de 10+5 est égal à ")+ str(10+5) #l'addition de 10 + 5 est égal à 15 
add=(100+1)*2;
print(a)
print(b)
print(c)
print(add)

semaine=["lundi","mardi","mercredi"]
print(semaine)
semaine.append("jeudi") 
semaine.remove(semaine[1])
print(semaine)

#les boucles 

#for  en affichant une liste de jeux 

jeux =["gta","mario","tekken","infamous","harry potter"]
for nom in jeux:
    print(nom)
#’on peut saisir un nombre dans la fonction  range()  , et qu’elle renvoie une séquence de nombres allant de 0 à ce nombre moins un.
for x in range(3):
    print(f"{x}, canette de bu")

#wile en lançant être des personnes tant qu il y a de la place 

place_cine=50
place_prise=10

while place_prise<place_cine:
      place_prise+=1
print(place_prise)

#pyramide 

nbrPierre=0
def creatPyramide() 
for nbr in range:
    