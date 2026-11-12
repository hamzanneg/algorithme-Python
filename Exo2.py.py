def bonjour():
    print("Bonjour")
    

def dibonjour(n):
    for i in range(n):
        print("Bonjour")
    

def renvoieBonjour(n):
    resultat = "Bonjour " * n
    return resultat

    

bonjour()

dibonjour(5)

print(renvoieBonjour(4))