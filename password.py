
password=str(input("veuillez choisir un mot de passe de d'au moins 10 caracter avec chiffre et lettre "))

if len(password)<8:
    print("veuilllez choisir un mdp plus long")
        #Vérifiez si tous les caractères du texte sont des chiffres :
elif password.isdigit():
    print("votre mot de passe ne contient que des chiffres")
elif password.isalpha():
    print("votre mot de passe ne contient  que des lettres")

else:
    print("inscription reussit") 
    

