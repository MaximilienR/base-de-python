nombres=[21,25,60,84,48,57,21]
nombre_pairs=nombre=[]

for i in nombres:
    nombre_pairs.append(i)
    if i%2==0:
        print("fizz")
    else: print("buzz")
