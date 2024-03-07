#exemple de création d'un objet en Python :

class Personne:
     def __init__(self, nom, age):
             self.nom = nom
             self.age = age

     def presentation(self):
             print(f"bonjour je m'appel  {self.nom} et j'ai   {self.age} ans")
 
    

# Création d'un objet de la classe Personne
personne1 = Personne("Smith", 35)
personne2 = Personne("Thomas Anderson", 30)

# Appel de la méthode afficher_infos pour afficher les informations de la personne
personne1.presentation()
personne2.presentation()

