# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:15:10 2021

@author: Bruno
"""
from job01 import Personne


class Livre:
    def __init__(self, titre):
        self.titre = titre
        #self.auteur = Auteur()

    def print(self):
        print(self.titre)

    def __str__(self):
        return self.titre


class Auteur(Personne):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.oeuvre = []

    def listerOeuvre(self):
        print(len(self.oeuvre), "oeuvre" +
              ("s" if (len(self.oeuvre) > 1) else "") + ":")
        for o in self.oeuvre:
            print(" " + str(o))

    def ecrireUnLivre(self, titre):
        livre = Livre(titre)
        self.oeuvre.append(livre)

    def titreDeLauteur(self, titre):
        for l in self.oeuvre:
            if l.titre == titre:
                return True
        return False
