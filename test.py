EX:1
"""
name = input("entrer votre nom:")
print("bienvenue" ,name, "!")
"""
EX:2
"""
a = int(input("entrer un nombre:"))
b = int(input("enter un autre nombre:"))

somme= a+b
differance= a-b
produit= a*b
division= a/b

print("la somme:",somme,)
print("la defferance:",differance,)
print("la produit:",produit,)
print("la division:",division,)
"""
EX:3
"""
x = int(input("entrer la largeur:"))
y =int(input("entrer la longeur:"))

p = 2 * (x+y)
print(p)
"""
EX:4
"""
c = int(input("entrer la temperature en c°:"))

F= (c*1.8)+32
print("la temperature en fahrenheit est:",F,)
"""
EX:5
"""

n = int(input("entrer le premier nombre:"))
v = int(input("entrer le deuxieme nombre:"))
w = int(input("entrer le troisieme nombre:"))

moyenne = (n+v+w)/3
print("la moyenne est:",moyenne,)
"""
EX:6
"""
pos = int(input("enter un nombre:"))

if pos > 0 :
    print("positif")
elif pos < 0:
    print ("nigatif")
else:
    print ("nul")
"""
EX:7
"""
o = int(input("entrer un nombre"))
if o % 2 == 0:
    print("pair")
else:
    print("impair")
"""
EX:8
"""
phrase = input("ecrire cette langage:")
if phrase == "python":
    print("correct")
else:
    print("incorrect")
"""
EX:9
"""
age = input("entrer votre age:")
if age >= 18:
    print("majeur")
else:
    print("mineur")
"""
EX:10
"""
nbr = int(input("entrer un nombre:"))
nbr2 = int(input("entrer un autre nombre:"))
if nbr > nbr2 :
    print("la premier nombre est grande")
if nbr < nbr2 :
    print("la deuxieme nombre est grande")
else:
    print("les deux nombre est egal")

"""
EX:11
"""
a = float(input("entrer votre note:"))
if a < 0 and a > 20:
    print("erreur")
if a >= 16:
    print("tres bien")
elif a >=14 and a < 16:
    print("bien")
elif a >=12 and a < 14:
    print("ase bien")
elif a >=10 and a < 12:
    print("passable")
else:
    print("redoublement")
"""
EX:12
"""
a = input("login:")
b = int(input("mot de pass:"))
if a == "admin" and b == 1234:
    print("bienvenue admin")
else:
    print("login ou mot de pass incorrect")
"""
EX:13
"""
a = int(input("l'anne aujourd'hui: "))
if a == 2026:
   print("correct")
else:
   print("incorrect")
"""
EX:14
"""
a = float(input("Entrez le premier côté : "))
b = float(input("Entrez le deuxième côté : "))
c = float(input("Entrez le troisième côté : "))

if a <= 0 or b <= 0 or c <= 0:
    print("Longueurs invalides")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Ce triangle n'existe pas")
elif a == b == c:
    print("Triangle équilatéral")
elif a == b or a == c or b == c:
    print("Triangle isocèle")
else:
    print("Triangle scalène")
"""
EX:15
"""
a = float(input("entrer un nombre:"))
b = float(input("entrer un autre nombre:"))
c = input("entrer l'opiration:")
if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
else:
    print("erreur")
"""
EX:16
"""

n = int(input("Entrez un entier : "))

if n % 3 == 0 and n % 5 == 0:
    print("Multiple de 3 et de 5")
elif n % 3 == 0:
    print("Multiple de 3")
elif n % 5 == 0:
    print("Multiple de 5")
else:
    print("Multiple ni de 3 ni de 5")

"""
EX:17
"""

H = int(input("Entrez l'heure (0-23) : "))

if H < 0 or H > 23:
    print("Heure invalide")
elif H < 12 and H >= 6:
    print("Matin")
elif H < 18 and H >= 12:
    print("Après-midi")
elif H < 21 and H >= 18:
    print("Soir")
else:
    print("Nuit")
"""
EX:18
"""
P = float(input("Entrez le prix : "))

if P > 100:
    R = P * 0.1
    P = P - R
    print("Réduction de 10 % appliquée")

print("Prix final :", P)
"""
EX:19
"""

mot = input("Entrez un mot : ")

longueur = len(mot)

print("Longueur du mot :", longueur)

if longueur > 5:
    print("La longueur est supérieure à 5")
else:
    print("La longueur n'est pas supérieure à 5")


"""
EX:20
"""

a = float(input("Entrez le premier côté : "))
b = float(input("Entrez le deuxième côté : "))
c = float(input("Entrez le troisième côté : "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Triangle valide")
else:
    print("Triangle invalide")
"""
EX:21
"""

note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))

moyenne = (note1 + note2) / 2

print("Moyenne :", moyenne)

if moyenne >= 10:
    print("Admis")
else:
    print("Non admis")

"""
EX:22
"""

revenu = float(input("Entrez votre revenu : "))
age = int(input("Entrez votre âge : "))

if revenu > 4000 and age < 60:
    print("Crédit accepté")
else:
    print("Crédit refusé")
"""
EX:23
"""

caractere = input("Entrez un caractère : ").lower()

if len(caractere) != 1 or not caractere.isalpha():
    print("Veuillez entrer une seule lettre")
elif caractere in "aeiouy":
    print("C'est une voyelle")
else:
    print("C'est une consonne")
"""
EX:24
"""

mois = int(input("Entrez le numéro du mois (1-12) : "))

if mois < 1 or mois > 12:
    print("Numéro de mois invalide")
elif mois in (3, 4, 5):
    print("Printemps")
elif mois in (6, 7, 8):
    print("Été")
elif mois in (9, 10, 11):
    print("Automne")
else:
    print("Hiver")
"""
EX:25
"""
mot_de_passe = input("Entrez votre mot de passe : ")

if len(mot_de_passe) >= 6:
    print("Mot de passe valide")
else:
    print("Mot de passe trop court!")
"""
for i in range(100):
    print(i)
if i == 100:
    i = 0
    print(i)

print(2**2**3)