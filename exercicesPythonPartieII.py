"""
def carre(n):
    resultat = n * n
    return resultat

def carre2():
    n = int(input("entrer le nombre:"))
    for i in range(1,n+1):
        resultat = carre(i)
        print(resultat)
    return resultat



print(carre(5))
carre2()
"""
"""
def demandeEntier():
    n = int(input("entrer un nombre:"))
    return n

def estEntre():
    a = int(input("entrer le nombre a:"))
    val = int(input("entrer le nombre val:"))
    b = int(input("entrer le nombre b:"))

    if a <= val <= b:
        return print(True)
    else:
        return print(False)

def demandeEntre(a,b):
    val = int(input("entrer un nombre val:"))
    if a <= val <= b:
        return print(True)
    while val < a or val > b:
        val = int(input("incorrect!,ressayer val:"))


z = int(input("entrer un nombre:"))
import random 
y = random.randint(1,10)
while z != y:
    z = int(input("perdu!, ressayer:"))
if z == y:
    print("gagner")

print(demandeEntier())
estEntre()
demandeEntre(1,5)
"""
"""
def mystere(n):
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return n>1

n = int(input("entrer un nombre n:"))
for i in range(1, n+1):
    if mystere(i):
        print(i)
"""
"""
def listeAleatoire(n):
    import random
    liste = []
    for i in range(n):
        liste.append(random.randint(1,10))
    return liste

print(listeAleatoire(20))
"""
"""
def maxliste():
    liste1 = []
    n = int(input("entrer le nombre de liste:"))
    for i in range(n):
        a = int(input("entrer les nombres:"))
        liste1.append(a)

    max = liste1[0]

    for i in range(n):
        if liste1[i] > max:
           max = liste1[i]

    print(liste1)
    return print(max)

maxliste()
"""
"""
def listeAleatoire(n):
    import random
    liste = []
    for i in range(n):
        liste.append(random.randint(1,10))
    max = liste[0]
    for i in range(n):
        if liste[i] > max:
            max = liste[i]
    print(liste)
    print(max)
    return liste

listeAleatoire(20)
"""
"""
def singltons():
    list = []
    n = int(input("entrer le nombre de liste:"))
    for i in range(n):
        import random
        y = random.randint(1,20)
        list.append(y)
    print(list)

    list2 =[]
    for element in list:
        if element not in list2:
            list2.append(element)
    print(list2)


singltons()
"""
"""
def listeAleatoire(n):
    import random
    liste = []
    liste2 =[]
    for i in range(n):
        liste.append(random.randint(1,10))

    for element in liste:
        if element not in liste2:
            liste2.append(element)
    
    max = liste[0]
    
    for i in range(n):
        if liste[i] > max:
            max = liste[i]
    print(liste)
    print(liste2)
    print(max)
    return liste

listeAleatoire(20)
"""
"""
def nbOccurences(n):
    liste1 = []
    container = 0
    b = int(input("entrer la taille de liste:"))
    for i in range(b):
        import random
        y = random.randint(1,10)
        liste1.append(y)

    for i in range(b):
        if n == liste1 [i]:
            container += 1

    print("nbOccurences(",n,liste1,")")
    print(container)
    return container

n = int(input("entrer le nombre pour recherche:"))
nbOccurences(n)
"""
"""
def listeAleatoire(n):
    import random
    liste = []
    liste2 =[]
    for i in range(n):
        liste.append(random.randint(1,10))

    for element in liste:
        if element not in liste2:
            liste2.append(element)
    
    max = liste[0]
    
    for i in range(n):
        if liste[i] > max:
            max = liste[i]

    print(liste)
    print(liste2)
    print(max)

    for i in range(n):
        container1 = liste.count(i)
        print(i,"apparait",container1)

    return liste

listeAleatoire(20)
"""
"""
def plusFrequent(a):
    liste = []
    
    import random
    for i in range(a):
        y = random.randint(1,10)
        liste.append(y)
    
    print(liste)
    max_count = 0
    nombre = 0

    for element in liste:
        if liste.count(element) > max_count:
            max_count = liste.count(element)
            nombre = element

    print("le nombre plus frequent est:",nombre) 
    print("il apparait", max_count, "fois")      

a = int(input("entrer la taille de la liste:"))
plusFrequent(a)
"""