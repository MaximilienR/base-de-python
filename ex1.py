 
""" 
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

users=["pierre","paul","jack"]
#verifier si un élement est présent dans une liste
def lapelle():
    if"jean" in users:
        print("pierre est présent dans la liste")
    else:
        print("cette personne n'est pas présent dans la liste")
lapelle()
"""
#nettoyer le code existant et corriger les bus 

class Personne:
    def __init__(self,nom:str,age:int,genre:bool):
        self.nom=nom
        self.age=age
        self.genre=genre 
        
    def SePresenter(self):
        print("bonjour, je m'appel"+self.nom+", j'ai "+str(self.age)+" ans")
        if self.genre==True:
            print("genre : Masculin")
            if self.EstMajeur():
                print("je suis majeur")
            else: 
                print("je suis mineur")
        else:     
            print("genre : Feminin")
            e_feminim=""
            if self.EstMajeur():
                e_feminim="e"
            if self.EstMajeur():
                print("je suis majeure"+e_feminim)
            else: 
                print("je suis mineure"+e_feminim)
        print()
    def EstMajeur(self):
        return self.age>=18
personne1=Personne("Pierre",30,genre=True)
personne1.SePresenter()

personne2=Personne("Lucy",15,genre=False)
personne2.SePresenter()
        