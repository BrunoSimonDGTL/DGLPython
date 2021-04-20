# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:31:11 2021

@author: Bruno
"""
import regex as re

PA="porte-avions"
CR = "croiseur"
CTORP ="contre-torpilleurs"
TORP = "torpilleur"

OrientationDirection = {"monte" : [0,+1],
                  "descent": [0,-1],
                  "gauche" : [+1,0],
                  "droite":  [-1,0]}

navireLongueur = {PA: 5,
                 CR : 4,
                 CTORP: 3,
                 TORP: 2}

class Navire :
    def __init__(self, proue, orientation, typeNavire):
        self.proue = proue
        self.orientation = orientation
        self.typeNavire = typeNavire

    def casesNavire(self):
        position =[self.proue]
        for length in range(navireLongueur[self.typeNavire]-1):
            x = position[-1][0] + OrientationDirection[self.orientation][0]
            y = position[-1][1] + OrientationDirection[self.orientation][1]
            position.append([x,y])
        return position

class Grille :
    def __init__(self, joueur):
        self.joueur = joueur
        self.navires =[]
        self.grille =[[0 for j in range(10)] for i in range(10)]
        self.listeNavire={PA: 1,
                 CR : 1,
                 CTORP: 2,
                 TORP: 1}

    def afficherGrille(self):
        #1er ligne
        print("   ", end="")
        for i in range(10) :
            print (" " +chr(ord('A')+i), end ="")
        print("")
        for y in range(10) :
            print((" " if y<9 else "") + str(y + 1), end=" ")
            for x  in range(10) :
                print(" " + str(self.grille[y][x]), end="")
            print("")
        print("")

    def placerNavire(self, type_navire):
        print("Placer un ", type_navire, "(",navireLongueur[type_navire], "cases)", end="")
        orientation= input("Choix de la direction (monte, descend, gauche, droite): ")
        if not orientation in OrientationDirection :
            print("Erreur d'orientation:", orientation)
            return False

        ligne = int(input("choix de la ligne: "))
        colonne = input ("Choix de la colonne: ")
        proue = [ligne,colonneToInt(colonne) ]
        if not(dansLaGrille(10, proue)) :
            print("Erreur position :", proue)
            return False

        navire = Navire(proue,orientation,type_navire)

        if self.bonnePosition(navire) :
            self.navires.append(navire)
            self.ajoutNavire(navire)
            return True
        else:
            return False


    def ajoutNavire(self,navire):
        for case in navire.casesNavire() :
            self.grille[case[1]-1][case[0]-1] = self.joueur

    def bonnePosition(self, navire):
        for case in navire.casesNavire() :

            if self.grille[case[1]-1][case[0]-1] == 0 and dansLaGrille(10, case):

                pass
            else:
                print("Impossible de mettre le bateau")
                return False
        return True

def dansLaGrille(taille,case) :
    return 0<case[0] and case[0]<=taille and 0<case[1] and case[1]<=taille

def findIntIntring(chaine):
    return [int(s) for s in re.findall(r'\b\d+\b', chaine)]

def colonneToInt(col):
    return ord('A') - ord(col.upper()) + 1

if __name__ == "__main__":
    #navire = Navire([1,5], "gauche", "torpilleur")
    #print(navire.casesNavire())
    gr=Grille(1)
    gr.afficherGrille()

    gr.placerNavire(PA)
    gr.afficherGrille()

