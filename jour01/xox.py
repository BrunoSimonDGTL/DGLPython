# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:09:06 2021

@author: Bruno
"""
import pygame as pg
import random
import sys

NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
JAUNE = (255, 255, 0)
GRIS = (240, 240, 240)


def in_bound(x, a, b):
    return a <= x and x <= b


def coupRandom(liste):
    return liste[random.randint(0, len(liste)-1)]
# ------------------------------------


class Jeu:

    def __init__(self):
        self.clock = pg.time.Clock()

        self.nb_case = 3
        self.window_size = 600
        self.case_size = self.window_size // self.nb_case
        self.ecran = pg.display.set_mode((self.window_size, self.window_size))
        pg.display.set_caption('TicTacToe1337 ')
        self.jeu_encours = True
        self.grille = Grille(self.ecran, self.case_size, self.nb_case)

        self.joueur_X = 'X'
        self.joueur_O = 'O'
        self.compteur = 0
        self.font = pg.font.SysFont(None, 30)
        self.type_X = 'Human'
        self.type_O = 'Machine'

    def fonction_principale(self):
        joueur = self.joueur_X
        type_j = self.type_X
        gagnant = False

        while self.jeu_encours and not gagnant:
            self.clock.tick(30)

            if type_j == 'Machine':

                indice_x, indice_y = coupRandom(self.grille.casesVide())

                self.compteur += self.grille.fixer_la_valeur(
                    indice_x, indice_y, joueur)

                gagnant = self.coup_a_gagne(indice_x, indice_y)
                if not gagnant:
                    joueur, type_j = self.change_player()
            else:

                for event in pg.event.get():

                    if event.type == pg.QUIT:
                        self.jeu_encours = False

                    if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0] \
                            and not gagnant and self.compteur < 9:

                        position = pg.mouse.get_pos()
                        indice_x = position[0]//self.case_size
                        indice_y = position[1]//self.case_size

                        self.compteur += self.grille.fixer_la_valeur(
                            indice_x, indice_y, joueur)

                        gagnant = self.coup_a_gagne(indice_x, indice_y)
                        if not gagnant:
                            joueur, type_j = self.change_player()

            self.ecran.fill(GRIS)
            self.grille.afficher()

            if gagnant:
                #print("Victoire de", joueur )
                img = self.font.render("Victoire de " + joueur, True, NOIR)
                self.ecran.blit(
                    img, (self.window_size//3 + 20, self.window_size//2))
            elif self.compteur == 9:
                #print("Match nul!")
                self.jeu_encours = False
                img = self.font.render("Match Nul", True, NOIR)
                self.ecran.blit(
                    img, (self.window_size//3 + 20, self.window_size//2))

            pg.display.flip()

    def change_player(self):
        if self.compteur % 2 == 0:
            return self.joueur_X, self.type_X

        else:
            return self.joueur_O, self.type_O

    def nb_pion_aligne(self, x, y):
        nbPions = 1
        list_direction = [(1, 1), (1, 0), (1, -1), (0, 1)]
        for direc in list_direction:
            nbPions = max(nbPions, self.nb_pions_dir(x, y, direc[0], direc[1]))
            if nbPions >= self.nb_case:
                return nbPions

        return nbPions

    def nb_pions_dir(self, x, y, inDirX, inDirY):  # return int

        lig = int()
        col = int()
        joueur = self.grille.grille[y][x]
        nbPions = 1

        lig = y + inDirY
        col = x + inDirX
        while in_bound(lig, 0, 2) and in_bound(col, 0, 2) and self.grille.grille[lig][col] == joueur:
            nbPions = nbPions + 1
            lig = lig + inDirY
            col = col + inDirX

        lig = y - inDirY
        col = x - inDirX
        while in_bound(lig, 0, 2) and in_bound(col, 0, 2) and self.grille.grille[lig][col] == joueur:
            nbPions = nbPions + 1
            lig = lig - inDirY
            col = col - inDirX

        # print("("+str(inDirX)+","+str(inDirY)+"):", nbPions) # affichage-test
        return nbPions

    def coup_a_gagne(self, x, y):
        return self.nb_case == self.nb_pion_aligne(x, y)


# ------------------------------------

class Grille:
    def __init__(self, ecran, size, nb_cases):
        self.ecran = ecran
        self.size = size
        self.nb_cases = nb_cases
        self.lignes = [((size, 0), (size, 3*size)),
                       ((2*size, 0), (2*size, 3*size)),
                       ((0, size), (3*size, size)),
                       ((0, 2*size), (3*size, 2*size)), ]
        self.grille = [[None for x in range(0, nb_cases)]
                       for y in range(0, nb_cases)]
        self.compteur_on = False

    def croix(self, x, y):
        size = self.size
        pg.draw.line(self.ecran, ROUGE,
                     (x * size+33, y * size+33),
                     (size + x * size - 33, size + y * size-33),
                     4)
        pg.draw.line(self.ecran, ROUGE,
                     (x * size + 33, size + y * size-33),
                     (size + x * size-33, y * size+33),
                     4)

    def cercle(self, x, y):
        size = self.size
        pg.draw.circle(self.ecran, JAUNE,
                       (size//2 + x * size, size//2 + y * size),
                       size//3,  4)

    def afficher(self):

        for ligne in self.lignes:
            pg.draw.line(self.ecran, NOIR, ligne[0], ligne[1], 2)

        for y in range(0, len(self.grille)):
            for x in range(0, len(self.grille)):
                if self.grille[y][x] == 'X':
                    self.croix(x, y)
                elif self.grille[y][x] == 'O':
                    self.cercle(x, y)

    def print_grille(self):
        for line in self.grille:
            print(line)

    def fixer_la_valeur(self, x, y, valeur):
        if self.grille[y][x] == None:
            self.grille[y][x] = valeur
            return 1
        else:
            return 0

    def casesVide(self):
        l = []
        for y in range(self.nb_cases):
            for x in range(self.nb_cases):
                if self.grille[y][x] == None:
                    l.append([x, y])

        return l
# ------------------------------------


if __name__ == '__main__':
    pg.init()
    Jeu().fonction_principale()
    pg.quit()
    sys.exit()
