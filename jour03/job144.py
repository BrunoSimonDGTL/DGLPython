# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:35:37 2021

@author: Bruno
"""

def afficherGrille(reinesPlacees, n):
    for ligne in range(n):
        for colonne in range(n):
            if reinesPlacees[ligne]  == colonne :
                print(' X', end='')
            else :
                print(' •', end='')
        print("")

#une dame par ligne, colonne et diagonale!

def estLibre (reinesPlacees, ligne, colonne) :
    #reinesPlacees[i] = colonne de la ieme dame placee sur le ligne i
    libre = True
    l = 0
    while l < ligne and libre:
        c = reinesPlacees[l]
        libre = colonne !=  c and abs(ligne - l) != abs(colonne - c)
        l += 1
    return libre

def placerReine(reinesPlacees, ligne, n, tot) :
    if ligne >= n :
        print("\nSolution", tot+1, ":")
        print("liste colonnes", reinesPlacees)
        afficherGrille(reinesPlacees,n)
        return tot + 1
    else:
        for colonne in range(n):
            if estLibre(reinesPlacees, ligne, colonne) :
                reinesPlacees[ligne]= colonne
                tot = placerReine(reinesPlacees, ligne+1, n, tot)
                reinesPlacees[ligne]= -1
        return tot


#n = int(input("Nombre de dame: "))
n = 8
tot = 0
listeReines = [-1 for i in [0]*n]

tot = placerReine(listeReines, 0, n, tot)

print("\nNombre de solutions pour", n, "Reines:", tot)




