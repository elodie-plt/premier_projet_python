# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:47:13 2019

@author: utilisateur
"""
from random import randint
entier = randint(1,1000)

print("Bienvenue dans l'émission intitulée : Le Juste Prix")

for nb_essais in range (1,11):
    print("il vous reste", 11-nb_essais,"essai(s).")
    entree=int(input("Entrez un prix:\n"))
    if nb_essais!=10:
        if entree < entier:
            print("C'est plus!")
        elif entree > entier:
            print("C'est moins!")
        else:
            break
#Ci-dessus, on vérifie seulement la condition de victoire#
if entree != entier:
    print("C'est perdu, Le juste prix était :", entier)
else:
    print("C'est gagné")

print("Merci d'avoir participé, A bientôt dans le Juste Prix")



