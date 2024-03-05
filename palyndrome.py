def check(word): 
    reverse=word[::-1]
    
    if (word == reverse): 
        return True
    return False

word= str(input("veuillez choisir un mot "))
if(check(word)):
        print("c'est un palyndrome")
else:
    print("c'est pas un palyndrome")
 
check(word) 

 