import random
mister=random.randint(1,10);

choiceUser =int(input("veuillez choisir un nombre "));

#def consigne(): 
if choiceUser<mister:
        print("veuillez saisir un nombre plus grand ")
        
elif choiceUser>mister:
             print("veuillez choisir un nombre plus petit" )
             
  #  while choiceUser != mister:
    #    consigne()
else:
        print("ok")
 
 