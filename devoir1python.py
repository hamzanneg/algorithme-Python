"""
ex1
"""
"""
d = float(input("entrer les deres:"))
m = float(input("entrer les minutes:"))
s = float(input("entrer les secondes:"))

angle = d + m / 60 + s / 3600
print("le resultat est:", angle)
"""
"""
ex2
"""
"""
import math
rad = float(input("entrer l'angle en radians:"))

deg = rad * 180 / math.pi

d = int(deg)

min = (deg - d) * 60

m = int(min)

s = (min - m) * 60

print("degres:", d)
print("minutes:", m)
print("secondes:", round(s))
"""
"""
ex3
"""
"""
a = int(input("entrer la temperature en C°:"))
b = a * 1.8 + 32
print("la temperature en F°:", b)
c = float(input("entrer la temperature en F°:"))
d = (c - 32) * 1.8
print("la temperature en C°:", d)
"""
"""
ex4
"""
"""
p = int(input("entrer votre capitalisation:"))
t = float(input("entrer votre taux d'interet:"))

for i in range(20):
    z = p + p*t/100
    p = z

print("capital final:", p)
"""
"""
ex5
"""
"""
g = 1
T = 0

for i in range(64):
    T = T + g
    g = g * 2

print("le nombre des grains est:", T)
print("{:.6e}".format(T))
"""
"""
ex6
"""
"""
a = input("entrer un texte:")
if "e" in a:
    print("e est exist!")
else:
    print("e n'exist pas!")
"""
"""
ex7
"""
"""
a = input("ecrire un texte:")
S = 0
for littre in a:
    if littre == "e":
        S = S + 1
else:
    print("e n'exist pas!")

print("e est exite", S ,"fois!")
"""
"""
ex8
"""
"""
a = input("ecrire un texte:")
b =""
for i in range(len(a)):
    b = b + a[i]

    if i < len(a) - 1:
        b = b + "*"
print(b)
"""
"""
ex9
"""
"""
a = input("ecrire un texte ou mot:")
b =""

for i in range(len(a)):
    b = b + a[ -1- i]

print(b)
"""
"""
ex10
"""
"""
a = input("ecrire un mot:")
b = ""

for i in range(len(a)-1, -1, -1):
    b = b + a[i]

if b == a:
    print("votre mot est palindrome!")
else:
    print("votre mot nest pas un palindrome!")
"""


